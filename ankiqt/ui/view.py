# -*- coding: utf-8 -*-
# Copyright: Damien Elmes <anki@ichi2.net>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import anki, anki.utils
from anki.sound import playFromText
from anki.latex import renderLatex, stripLatex
from anki.utils import stripHTML
from anki.hooks import runHook, runFilter
from anki.media import stripMedia
import types, time, re, os, urllib, sys, difflib
from ankiqt import ui
from ankiqt.ui.utils import mungeQA, getBase
from anki.utils import fmtTimeSpan
from PyQt4.QtWebKit import QWebPage, QWebView

failedCharColour = "#FF0000"
passedCharColour = "#00FF00"
futureWarningColour = "#FF0000"

# Views - define the way a user is prompted for questions, etc
##########################################################################

class View(object):
    "Handle the main window update as we transition through various states."

    def __init__(self, parent, body, frame=None):
        self.main = parent
        self.body = body
        self.frame = frame
        self.main.connect(self.body, SIGNAL("loadFinished(bool)"),
                          self.onLoadFinished)

    # State control
    ##########################################################################

    def setState(self, state):
        "Change to STATE, and update the display."
        self.oldState = getattr(self, 'state', None)
        self.state = state
        if self.state == "initial":
            return
        elif self.state == "noDeck":
            self.clearWindow()
            self.drawWelcomeMessage()
            self.flush()
            return
        self.redisplay()

    def redisplay(self):
        "Idempotently display the current state (prompt for question, etc)"
        if self.state == "noDeck" or self.state == "studyScreen":
            return
        self.buffer = ""
        self.haveTop = (self.main.lastCard and (
            self.main.config['showLastCardContent'] or
            self.main.config['showLastCardInterval'])) or (
            self.needFutureWarning())
        self.drawRule = (self.main.config['qaDivider'] and
                         self.main.currentCard and
                         not self.main.currentCard.cardModel.questionInAnswer)
        if not self.main.deck.isEmpty():
            if self.haveTop:
                self.drawTopSection()
        if self.state == "showQuestion":
            self.setBackground()
            self.drawQuestion()
            if self.drawRule:
                self.write("<hr>")
        elif self.state == "showAnswer":
            self.setBackground()
            if not self.main.currentCard.cardModel.questionInAnswer:
                self.drawQuestion(nosound=True)
            if self.drawRule:
                self.write("<hr>")
            self.drawAnswer()
        elif self.state == "deckEmpty":
            self.drawWelcomeMessage()
        elif self.state == "deckFinished":
            self.drawDeckFinishedMessage()
        self.flush()

    def addStyles(self):
        # card styles
        s = "<style>\n"
        if self.main.deck:
            s += self.main.deck.css
        s += "div { white-space: pre-wrap; }\n"
        s = runFilter("addStyles", s, self.main.currentCard)
        s += "</style>"
        return s

    def clearWindow(self):
        self.body.setHtml("")
        self.buffer = ""

    def setBackground(self):
        col = self.main.currentCard.cardModel.lastFontColour
        self.write("<style>html { background: %s;}</style>" % col)

    # Font properties & output
    ##########################################################################

    def flush(self):
        "Write the current HTML buffer to the screen."
        self.buffer = self.addStyles() + self.buffer
        # hook for user css
        runHook("preFlushHook")
        self.buffer = '''<html><head>%s</head><body>%s</body></html>''' % (
            getBase(self.main.deck, self.main.currentCard), self.buffer)
        #print self.buffer.encode("utf-8")
        self.body.setHtml(self.buffer)

    def write(self, text):
        if type(text) != types.UnicodeType:
            text = unicode(text, "utf-8")
        self.buffer += text

    # Question and answer
    ##########################################################################

    def center(self, str, height=40):
        if not self.main.config['splitQA']:
            return "<center>" + str + "</center>"
        return '''\
<center><div style="display: table; height: %s%%; width:100%%; overflow: hidden;">\
<div style="display: table-cell; vertical-align: middle;">\
<div style="">%s</div></div></div></center>''' % (height, str)

    def drawQuestion(self, nosound=False):
        "Show the question."
        if not self.main.config['splitQA']:
            self.write("<br>")
        q = self.main.currentCard.htmlQuestion()
        if self.haveTop:
            height = 35
        elif self.main.currentCard.cardModel.questionInAnswer:
            height = 40
        else:
            height = 45
        q = runFilter("drawQuestion", q, self.main.currentCard)
        self.write(self.center(self.mungeQA(self.main.deck, q), height))
        if self.state != self.oldState and not nosound:
            playFromText(q)

    def correct(self, a, b):
        if b == "":
            return "";

        ret = "";
        s = difflib.SequenceMatcher(None, b, a)

        sz = self.main.currentCard.cardModel.answerFontSize
        fn = self.main.currentCard.cardModel.answerFontFamily
        st = "background: %s; color: #000; font-size: %dpx; font-family: %s;"
        ok = st % (passedCharColour, sz, fn)
        bad = st % (failedCharColour, sz, fn)

        for tag, i1, i2, j1, j2 in s.get_opcodes():
            if tag == "equal":
                ret += ("<span style='%s'>%s</span>" % (ok, b[i1:i2]))
            elif tag == "replace":
                ret += ("<span style='%s'>%s</span>"
                        % (bad, b[i1:i2] + (" " * ((j2 - j1) - (i2 - i1)))))
            elif tag == "delete":
                p = re.compile(r"^\s*$")
                if p.match(b[i1:i2]):
                    ret += ("<span style='%s'>%s</span>" % (ok, b[i1:i2]))
                else:
                    ret += ("<span style='%s'>%s</span>" % (bad, b[i1:i2]))
            elif tag == "insert":
                ret += ("<span style='%s'>%s</span>" % (bad, " " * (j2 - j1)))
        return ret

    def drawAnswer(self):
        "Show the answer."
        a = self.main.currentCard.htmlAnswer()
        a = runFilter("drawAnswer", a, self.main.currentCard)
        if self.main.currentCard.cardModel.typeAnswer:
            try:
                cor = stripMedia(stripHTML(self.main.currentCard.fact[
                    self.main.currentCard.cardModel.typeAnswer]))
            except KeyError:
                self.main.currentCard.cardModel.typeAnswer = ""
                cor = ""
            if cor:
                given = unicode(self.main.typeAnswerField.text())
                res = self.correct(cor, given)
                a = res + "<br>" + a
        self.write(self.center('<span id=answer />'
                               + self.mungeQA(self.main.deck, a)))
        if self.state != self.oldState:
            playFromText(a)

    def mungeQA(self, deck, txt):
        txt = mungeQA(deck, txt)
        # hack to fix thai presentation issues
        if self.main.config['addZeroSpace']:
            txt = txt.replace("</span>", "&#8203;</span>")
        return txt

    def onLoadFinished(self, bool):
        if self.state == "showAnswer":
            if self.main.config['scrollToAnswer']:
                mf = self.body.page().mainFrame()
                mf.evaluateJavaScript("location.hash = 'answer'")

    # Top section
    ##########################################################################

    def drawTopSection(self):
        "Show previous card, next scheduled time, and stats."
        self.buffer += "<center>"
        self.drawFutureWarning()
        self.drawLastCard()
        self.buffer += "</center>"

    def needFutureWarning(self):
        if not self.main.currentCard:
            return
        if self.main.currentCard.due <= time.time():
            return
        if self.main.currentCard.due - time.time() <= self.main.deck.delay0:
            return
        return True

    def drawFutureWarning(self):
        if not self.needFutureWarning():
            return
        self.write("<span style='color: %s'>" % futureWarningColour +
                   _("This card was due in %s.") % fmtTimeSpan(
            self.main.currentCard.due - time.time(), after=True) +
                   "</span>")

    def drawLastCard(self):
        "Show the last card if not the current one, and next time."
        if self.main.lastCard:
            if self.main.config['showLastCardContent']:
                if (self.state == "deckFinished" or
                    self.main.currentCard.id != self.main.lastCard.id):
                    q = self.main.lastCard.question.replace("<br>", "  ")
                    q = stripHTML(q)
                    if len(q) > 50:
                        q = q[:50] + "..."
                    a = self.main.lastCard.answer.replace("<br>", "  ")
                    a = stripHTML(a)
                    if len(a) > 50:
                        a = a[:50] + "..."
                    s = "%s<br>%s" % (q, a)
                    s = stripLatex(s)
                    self.write('<span class="lastCard">%s</span><br>' % s)
            if self.main.config['showLastCardInterval']:
                if self.main.lastQuality > 1:
                    msg = _("Well done! This card will appear again in "
                            "<b>%(next)s</b>.") % \
                            {"next":self.main.lastScheduledTime}
                else:
                    msg = _("This card will appear again later.")
                self.write(msg)
            self.write("<br>")

    # Welcome/empty/finished deck messages
    ##########################################################################

    def drawWelcomeMessage(self):
        self.main.mainWin.welcomeText.setText("""\
<h1>%(welcome)s</h1>
<p>
<table>

<tr>
<td width=50>
<a href="welcome:addfacts"><img src=":/icons/list-add.png"></a>
</td>
<td valign=middle><h1><a href="welcome:addfacts">%(add)s</a></h1>
%(start)s</td>
</tr>

</table>

<br>
<table>

<tr>
<td width=50>
<a href="welcome:back"><img src=":/icons/go-previous.png"></a>
</td>
<td valign=middle><h2><a href="welcome:back">%(back)s</a></h2></td>
</tr>

</table>""" % \
	{"welcome":_("Welcome to Anki!"),
         "add":_("Add Material"),
         "start":_("Start adding your own material."),
         "back":_("Back to Deck Browser"),
         })

    def drawDeckFinishedMessage(self):
        "Tell the user the deck is finished."
        self.main.mainWin.congratsLabel.setText(
            self.main.deck.deckFinishedMsg())

class AnkiWebView(QWebView):

    def __init__(self, *args):
        QWebView.__init__(self, *args)
        self.setObjectName("mainText")

    def keyPressEvent(self, evt):
        if evt.matches(QKeySequence.Copy):
            self.triggerPageAction(QWebPage.Copy)
            evt.accept()
        evt.ignore()

    def contextMenuEvent(self, evt):
        QWebView.contextMenuEvent(self, evt)

    def dropEvent(self, evt):
        pass
