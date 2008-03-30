# -*- coding: utf-8 -*-
# Copyright: Damien Elmes <anki@ichi2.net>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import re, os, sys
from anki.utils import parseTags, stripHTML
import anki.sound
from ankiqt import ui

class FactEditor(object):
    """An editor for new/existing facts.

    The fact is updated as it is edited.
    Extra widgets can be added to 'fieldsGrid' to represent card-specific
    information, etc."""

    def __init__(self, parent, widget, deck=None):
        self.widget = widget
        self.parent = parent
        self.deck = deck
        self.fact = None
        self.fontChanged = False
        self.setupFields()
        self.checkTimer = None
        self.onChange = None
        self.onFactValid = None
        self.onFactInvalid = None
        self.lastFocusedEdit = None

    def setFact(self, fact, noFocus=False, check=False):
        "Make FACT the current fact."
        self.fact = fact
        self.factState = None
        if self.needToRedraw():
            self.drawFields(noFocus, check)
        else:
            self.updateFields(check)
        if not noFocus:
            # update focus to first field
            self.fields[self.fact.fields[0].name][1].setFocus()
        self.fontChanged = False

    def setupFields(self):
        self.fields = {}
        # top level vbox
        self.fieldsBox = QVBoxLayout(self.widget)
        self.fieldsBox.setMargin(5)
        self.fieldsBox.setSpacing(3)
        # icons
        self.iconsBox = QHBoxLayout()
        self.fieldsBox.addLayout(self.iconsBox)
        # scrollarea
        self.fieldsScroll = QScrollArea()
        self.fieldsScroll.setWidgetResizable(True)
        self.fieldsScroll.setLineWidth(0)
        self.fieldsScroll.setFrameStyle(0)
        self.fieldsScroll.setFocusPolicy(Qt.NoFocus)
        self.fieldsBox.addWidget(self.fieldsScroll)
        self.iconsBox.setMargin(0)
        self.iconsBox.addItem(QSpacerItem(20,20, QSizePolicy.Expanding))
        # button styles for mac
        self.plastiqueStyle = QStyleFactory.create("plastique")
        # bold
        self.bold = QPushButton()
        self.bold.setCheckable(True)
        self.bold.connect(self.bold, SIGNAL("toggled(bool)"), self.toggleBold)
        self.bold.setIcon(QIcon(":/icons/text_bold.png"))
        self.bold.setToolTip(_("Bold text"))
        self.bold.setShortcut(_("Ctrl+b"))
        self.bold.setFocusPolicy(Qt.NoFocus)
        self.bold.setEnabled(False)
        self.iconsBox.addWidget(self.bold)
        self.bold.setStyle(self.plastiqueStyle)
        # italic
        self.italic = QPushButton(self.widget)
        self.italic.setCheckable(True)
        self.italic.connect(self.italic, SIGNAL("toggled(bool)"), self.toggleItalic)
        self.italic.setIcon(QIcon(":/icons/text_italic.png"))
        self.italic.setToolTip(_("Italic text"))
        self.italic.setShortcut(_("Ctrl+i"))
        self.italic.setFocusPolicy(Qt.NoFocus)
        self.italic.setEnabled(False)
        self.iconsBox.addWidget(self.italic)
        self.italic.setStyle(self.plastiqueStyle)
        # underline
        self.underline = QPushButton(self.widget)
        self.underline.setCheckable(True)
        self.underline.connect(self.underline, SIGNAL("toggled(bool)"), self.toggleUnderline)
        self.underline.setIcon(QIcon(":/icons/text_under.png"))
        self.underline.setToolTip(_("Underline text"))
        self.underline.setShortcut(_("Ctrl+u"))
        self.underline.setFocusPolicy(Qt.NoFocus)
        self.underline.setEnabled(False)
        self.iconsBox.addWidget(self.underline)
        self.underline.setStyle(self.plastiqueStyle)
        # foreground color - not working on mac
        self.foreground = QPushButton()
        self.foreground.connect(self.foreground, SIGNAL("clicked()"), self.selectForeground)
        self.foreground.setToolTip(_("Foreground colour"))
        self.foreground.setShortcut(_("Ctrl+r"))
        self.foreground.setFocusPolicy(Qt.NoFocus)
        self.foreground.setEnabled(False)
        self.foreground.setFixedWidth(30)
        self.foregroundFrame = QFrame()
        self.foregroundFrame.setAutoFillBackground(True)
        hbox = QHBoxLayout()
        hbox.addWidget(self.foregroundFrame)
        hbox.setMargin(5)
        self.foreground.setLayout(hbox)
        self.iconsBox.addWidget(self.foreground)
        self.foreground.setStyle(self.plastiqueStyle)
        # pictures
        spc = QSpacerItem(10,10)
        self.iconsBox.addItem(spc)
        self.addPicture = QPushButton(self.widget)
        self.addPicture.connect(self.addPicture, SIGNAL("clicked()"), self.onAddPicture)
        self.addPicture.setFocusPolicy(Qt.NoFocus)
        self.addPicture.setShortcut(_("Ctrl+p"))
        self.addPicture.setIcon(QIcon(":/icons/colors.png"))
        self.addPicture.setEnabled(False)
        self.addPicture.setToolTip(_("Add a picture"))
        self.iconsBox.addWidget(self.addPicture)
        self.addPicture.setStyle(self.plastiqueStyle)
        # sounds
        self.addSound = QPushButton(self.widget)
        self.addSound.connect(self.addSound, SIGNAL("clicked()"), self.onAddSound)
        self.addSound.setFocusPolicy(Qt.NoFocus)
        self.addSound.setShortcut(_("Ctrl+s"))
        self.addSound.setEnabled(False)
        self.addSound.setIcon(QIcon(":/icons/arts.png"))
        self.addSound.setToolTip(_("Add audio"))
        self.iconsBox.addWidget(self.addSound)
        self.addSound.setStyle(self.plastiqueStyle)
        # latex
        spc = QSpacerItem(10,10)
        self.iconsBox.addItem(spc)
        self.latex = QPushButton(self.widget)
        self.latex.connect(self.latex, SIGNAL("clicked()"), self.insertLatex)
        self.latex.setToolTip(_("Latex"))
        self.latex.setShortcut(_("Ctrl+l"))
        self.latex.setIcon(QIcon(":/icons/tex.png"))
        self.latex.setFocusPolicy(Qt.NoFocus)
        self.latex.setEnabled(False)
        self.iconsBox.addWidget(self.latex)
        self.latex.setStyle(self.plastiqueStyle)
        # latex eqn
        self.latexEqn = QPushButton(self.widget)
        self.latexEqn.connect(self.latexEqn, SIGNAL("clicked()"), self.insertLatexEqn)
        self.latexEqn.setToolTip(_("Latex equation"))
        self.latexEqn.setShortcut(_("Ctrl+e"))
        self.latexEqn.setIcon(QIcon(":/icons/math_sqrt.png"))
        self.latexEqn.setFocusPolicy(Qt.NoFocus)
        self.latexEqn.setEnabled(False)
        self.iconsBox.addWidget(self.latexEqn)
        self.latexEqn.setStyle(self.plastiqueStyle)
        # latex math env
        self.latexMathEnv = QPushButton(self.widget)
        self.latexMathEnv.connect(self.latexMathEnv, SIGNAL("clicked()"),
                                  self.insertLatexMathEnv)
        self.latexMathEnv.setToolTip(_("Latex math environment"))
        self.latexMathEnv.setShortcut(_("Ctrl+m"))
        self.latexMathEnv.setIcon(QIcon(":/icons/math_matrix.png"))
        self.latexMathEnv.setFocusPolicy(Qt.NoFocus)
        self.latexMathEnv.setEnabled(False)
        self.iconsBox.addWidget(self.latexMathEnv)
        self.latexMathEnv.setStyle(self.plastiqueStyle)

        self.fieldsFrame = None
        self.widget.setLayout(self.fieldsBox)
        self.updatingFields = False

    def _makeGrid(self):
        "Rebuild the grid to avoid trigging QT bugs."
        self.fieldsFrame = QFrame()
        self.fieldsFrame.setFrameStyle(0)
        self.fieldsFrame.setLineWidth(0)
        self.fieldsGrid = QGridLayout(self.fieldsFrame)
        self.fieldsFrame.setLayout(self.fieldsGrid)
        self.fieldsGrid.setMargin(0)

    def drawFields(self, noFocus=False, check=False):
        self.parent.setUpdatesEnabled(False)
        self._makeGrid()
        # add entries for each field
        fields = self.fact.fields
        self.fields = {}
        n = 0
        first = None
        for field in fields:
            # label
            l = QLabel(field.name)
            self.fieldsGrid.addWidget(l, n, 0)
            # edit widget
            w = FactEdit(self)
            w.setTabChangesFocus(True)
            w.setAcceptRichText(True)
            w.setMinimumSize(20, 60)
            w.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            w.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.fieldsGrid.addWidget(w, n, 1)
            self.fields[field.name] = (field, w)
            # catch changes
            w.connect(w, SIGNAL("textChanged()"),
                      lambda f=field, w=w: self.fieldChanged(f, w))
            w.connect(w, SIGNAL("currentCharFormatChanged(QTextCharFormat)"),
                      lambda w=w: self.formatChanged(w))
            n += 1
        # tags
        self.fieldsGrid.addWidget(QLabel(_("Tags")), n, 0)
        self.tags = ui.tagedit.TagEdit(self.parent)
        self.tags.connect(self.tags, SIGNAL("textChanged(QString)"),
                          self.onTagChange)
        # update available tags
        self.tags.setDeck(self.deck)
        self.fieldsGrid.addWidget(self.tags, n, 1)
        # update fields
        self.updateFields(check)
        self.parent.setUpdatesEnabled(True)
        self.fieldsScroll.setWidget(self.fieldsFrame)

    def needToRedraw(self):
        if len(self.fact.fields) != len(self.fields):
            return True
        for field in self.fact.fields:
            if field.name not in self.fields:
                return True
        return self.fontChanged

    def updateFields(self, check=True, font=True):
        "Update field text (if changed) and font/colours."
        self.updatingFields = True
        # text
        for (name, (field, w)) in self.fields.items():
            new = self.fact[name]
            old = self.pruneHTML(unicode(w.toHtml()))
            # only update if something has changed, to preserve the cursor
            if new != old:
                w.setHtml(new)
            if font:
                # apply fonts
                font = QFont()
                # family
                family = (field.fieldModel.editFontFamily or
                          field.fieldModel.quizFontFamily)
                if family:
                    font.setFamily(family)
                # size
                size = (field.fieldModel.editFontSize or
                        field.fieldModel.quizFontSize)
                if size:
                    font.setPixelSize(size)
                w.setFont(font)
        self.tags.blockSignals(True)
        self.tags.setText(self.fact.tags)
        self.tags.blockSignals(False)
        self.updatingFields = False
        if check:
            self.checkValid()

    def fieldChanged(self, field, widget):
        if self.updatingFields:
            return
        value = self.pruneHTML(unicode(widget.toHtml()))
        if value and not value.strip():
            widget.setText("")
            value = u""
        self.fact[field.name] = value
        self.fact.setModified(textChanged=True)
        self.deck.setModified()
        self.fact.onKeyPress(field, value)
        # the keypress handler may have changed something, so update all
        self.updateFields(font=False)
        if self.onChange:
            self.onChange(field)
        self.scheduleCheck()
        self.formatChanged(None)

    def pruneHTML(self, html):
        "Remove cruft like body tags and return just the important part."
        html = re.sub(".*<body.*?>(.*)</body></html>",
                      "\\1", html.replace("\n", u""))
        html = re.sub('<p style=".*?">(.*?)</p>', u'\\1<br>', html)
        html = re.sub('<br>$', u'', html)
        return html

    def scheduleCheck(self):
        if not self.deck:
            return
        interval = 200
        if self.checkTimer:
            self.checkTimer.setInterval(interval)
        else:
            self.checkTimer = QTimer(self.parent)
            self.checkTimer.setSingleShot(True)
            self.checkTimer.start(interval)
            self.parent.connect(self.checkTimer, SIGNAL("timeout()"),
                                self.checkValid)

    def checkValid(self):
        empty = []
        dupe = []
        problems = []
        for field in self.fact.fields:
            p = QPalette()
            if not self.fact.fieldValid(field):
                empty.append(field)
                p.setColor(QPalette.Base, QColor("#ffffcc"))
                self.fields[field.name][1].setPalette(p)
            elif not self.fact.fieldUnique(field, self.deck.s):
                dupe.append(field)
                p.setColor(QPalette.Base, QColor("#ffcccc"))
                self.fields[field.name][1].setPalette(p)
            else:
                p.setColor(QPalette.Base, QColor("#ffffff"))
                self.fields[field.name][1].setPalette(p)
        self.checkTimer = None
        # call relevant hooks
        invalid = len(empty+dupe)
        if self.factState != "valid" and not invalid:
            if self.onFactValid:
                self.onFactValid(self.fact)
            self.factState = "valid"
        elif self.factState != "invalid" and invalid:
            if self.onFactInvalid:
                self.onFactInvalid(self.fact)
            self.factState = "invalid"

    def onTagChange(self, text):
        if not self.updatingFields:
            self.fact.tags = unicode(text)
        if self.onChange:
            self.onChange(None)

    def focusField(self, fieldName):
        self.fields[fieldName][1].setFocus()

    def formatChanged(self, fmt):
        w = self.focusedEdit()
        if not w or w.textCursor().hasSelection():
            return
        else:
            self.bold.setChecked(w.fontWeight() == QFont.Bold)
            self.italic.setChecked(w.fontItalic())
            self.underline.setChecked(w.fontUnderline())
            self.foregroundFrame.setPalette(QPalette(w.textColor()))

    def resetFormatButtons(self):
        self.bold.setChecked(False)
        self.italic.setChecked(False)
        self.underline.setChecked(False)

    def enableButtons(self, val=True):
        self.bold.setEnabled(val)
        self.italic.setEnabled(val)
        self.underline.setEnabled(val)
        self.foreground.setEnabled(val)
        self.addPicture.setEnabled(val)
        self.addSound.setEnabled(val)
        self.latex.setEnabled(val)
        self.latexEqn.setEnabled(val)
        self.latexMathEnv.setEnabled(val)

    def disableButtons(self):
        self.enableButtons(False)

    def focusedEdit(self):
        for (name, (field, w)) in self.fields.items():
            if w.hasFocus():
                return w
        return None

    def toggleBold(self, bool):
        w = self.focusedEdit()
        if w:
            self.fontChanged = True
            w.setFontWeight(bool and QFont.Bold or QFont.Normal)

    def toggleItalic(self, bool):
        w = self.focusedEdit()
        if w:
            self.fontChanged = True
            w.setFontItalic(bool)

    def toggleUnderline(self, bool):
        w = self.focusedEdit()
        if w:
            self.fontChanged = True
            w.setFontUnderline(bool)

    def selectForeground(self):
        w = self.focusedEdit()
        if w:
            # we lose the selection when we open the colour dialog on win32,
            # so we need to save it
            cursor = w.textCursor()
            new = QColorDialog.getColor(w.textColor(), self.parent)
            if new.isValid():
                w.setTextCursor(cursor)
                self.foregroundFrame.setPalette(QPalette(new))
                w.setTextColor(new)
                # now we clear the selection
                cursor.clearSelection()
                w.setTextCursor(cursor)
            self.fontChanged = True

    def insertLatex(self):
        w = self.focusedEdit()
        if w:
            w.insertHtml("[latex][/latex]")
            w.moveCursor(QTextCursor.PreviousWord)
            w.moveCursor(QTextCursor.PreviousCharacter)

    def insertLatexEqn(self):
        w = self.focusedEdit()
        if w:
            w.insertHtml("[$][/$]")
            w.moveCursor(QTextCursor.PreviousWord)
            w.moveCursor(QTextCursor.PreviousCharacter)

    def insertLatexMathEnv(self):
        w = self.focusedEdit()
        if w:
            w.insertHtml("[$$][/$$]")
            w.moveCursor(QTextCursor.PreviousWord)
            w.moveCursor(QTextCursor.PreviousCharacter)

    def fieldsAreBlank(self):
        for (field, widget) in self.fields.values():
            value = self.pruneHTML(unicode(widget.toHtml()))
            if value:
                return False
        return True

    def onAddPicture(self):
        if not self.hasMediaDir():
            return
        # get this before we open the dialog
        w = self.focusedEdit()
        key = _("Images (*.jpg *.png)")
        file = ui.utils.getFile(self.parent, _("Add an image"), "picture", key)
        if not file:
            return
        path = self.deck.addMedia(file)
        w.insertHtml('<img src="%s">' % path)

    def onAddSound(self):
        if not self.hasMediaDir():
            return
        # get this before we open the dialog
        w = self.focusedEdit()
        key = _("Sounds (*.mp3 *.ogg *.wav)")
        file = ui.utils.getFile(self.parent, _("Add audio"), "audio", key)
        if not file:
            return
        anki.sound.play(file)
        path = self.deck.addMedia(file)
        w.insertHtml('[sound:%s]' % path)

    def hasMediaDir(self):
        if self.deck.mediaDir(create=True):
            return True
        ui.utils.showInfo("Please save your deck first.", self.parent)
        return False

class FactEdit(QTextEdit):

    def __init__(self, parent, *args):
        QTextEdit.__init__(self, *args)
        self.parent = parent

    def insertFromMimeData(self, source):
        if source.hasText():
            self.insertPlainText(source.text())
        elif source.hasHtml():
            self.insertHtml(self.tidyHTML(unicode(source.html())))

    def tidyHTML(self, html):
        # FIXME: support pre tags
        html = re.sub("\n", " ", html)
        html = re.sub("<br ?/?>", "\n", html)
        html = re.sub("<p ?/?>", "\n\n", html)
        html = re.sub('<style type="text/css">.*?</style>', "", html)
        html = stripHTML(html)
        html = html.replace("\n", "<br>")
        html = re.sub("\s\s+", " ", html).strip()
        return html

    def focusOutEvent(self, evt):
        QTextEdit.focusOutEvent(self, evt)
        self.parent.lastFocusedEdit = self
        self.parent.resetFormatButtons()
        self.parent.disableButtons()

    def focusInEvent(self, evt):
        if (self.parent.lastFocusedEdit and
            self.parent.lastFocusedEdit is not self):
            # remove selection from previous widget
            try:
                cur = self.parent.lastFocusedEdit.textCursor()
                cur.clearSelection()
                self.parent.lastFocusedEdit.setTextCursor(cur)
            except RuntimeError:
                # old widget was deleted
                pass
            self.lastFocusedEdit = None
        QTextEdit.focusInEvent(self, evt)
        self.parent.formatChanged(None)
        self.parent.enableButtons()
