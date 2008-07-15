# Copyright: Damien Elmes <anki@ichi2.net>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import anki
from anki import stdmodels
from anki.models import *
from ankiqt import ui
import ankiqt.forms

class ModelChooser(QHBoxLayout):

    def __init__(self, parent, main, deck, onChangeFunc, cards=True):
        QHBoxLayout.__init__(self)
        self.parent = parent
        self.main = main
        self.deck = deck
        self.onChangeFunc = onChangeFunc
        self.setMargin(0)
        self.setSpacing(6)
        label = QLabel(_("<b><u>M</u>odel</b>:"))
        self.addWidget(label)
        self.models = QComboBox()
        s = QShortcut(QKeySequence(_("Alt+M")), self.parent)
        s.connect(s, SIGNAL("activated()"),
                  lambda: self.models.showPopup())
        self.drawModels()
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy(7),
            QSizePolicy.Policy(0))
        self.models.setSizePolicy(sizePolicy)
        self.addWidget(self.models)
        self.add = QPushButton()
        self.add.setIcon(QIcon(":/icons/add.png"))
        self.add.setToolTip(_("Add a new model"))
        self.add.setAutoDefault(False)
        self.addWidget(self.add)
        self.connect(self.add, SIGNAL("clicked()"), self.onAdd)
        self.edit = QPushButton()
        self.edit.setIcon(QIcon(":/icons/edit.png"))
        self.edit.setShortcut(_("Alt+E"))
        self.edit.setToolTip(_("Edit the current model"))
        self.edit.setAutoDefault(False)
        self.addWidget(self.edit)
        self.connect(self.edit, SIGNAL("clicked()"), self.onEdit)
        self.connect(self.models, SIGNAL("activated(int)"), self.onChange)
        self.handleCards = False
        if cards:
            self.handleCards = True
            label = QLabel(_("<b><u>C</u>ards</b>:"))
            self.addWidget(label)
            self.cards = QPushButton()
            self.connect(self.cards, SIGNAL("clicked()"), self.onCardChange)
            s = QShortcut(QKeySequence(_("Alt+C")), self.parent)
            s.connect(s, SIGNAL("activated()"),
                      self.onCardChange)
            self.addWidget(self.cards)
            self.drawCardModels()

    def show(self):
        for i in range(self.count()):
            self.itemAt(i).widget().show()

    def hide(self):
        for i in range(self.count()):
            self.itemAt(i).widget().hide()

    def onEdit(self):
        idx = self.models.currentIndex()
        model = self.deck.models[idx]
        ui.modelproperties.ModelProperties(self.parent, model, self.main,
                                           onFinish=self.onModelEdited)
        self.drawModels()
        self.changed(model)

    def onModelEdited(self):
        self.drawModels()

    def onAdd(self):
        model = AddModel(self.parent, self.main).getModel()
        if model:
            self.deck.addModel(model)
            self.drawModels()
            self.changed(model)
            self.deck.setModified()

    def onChange(self, idx):
        model = self.deck.models[idx]
        self.deck.currentModel = model
        self.changed(model)
        self.deck.setModified()

    def changed(self, model):
        self.deck.addModel(model)
        self.onChangeFunc(model)
        self.drawCardModels()

    def drawModels(self):
        self.models.clear()
        self.models.addItems(QStringList(
            [m.name for m in self.deck.models]))
        idx = self.deck.models.index(self.deck.currentModel)
        self.models.setCurrentIndex(idx)

    def drawCardModels(self):
        if not self.handleCards:
            return
        m = self.deck.currentModel
        txt = ", ".join([c.name for c in m.cardModels if c.active])
        if len(txt) > 30:
            txt = txt[0:30] + "..."
        self.cards.setText(txt)

    def onCardChange(self):
        m = QMenu(self.parent)
        m.setTitle("menu")
        model = self.deck.currentModel
        for card in model.cardModels:
            action = QAction(self.parent)
            action.setCheckable(True)
            if card.active:
                action.setChecked(True)
            action.setText(card.name)
            self.connect(action, SIGNAL("toggled(bool)"),
                         lambda b, a=action, c=card: \
                         self.cardChangeTriggered(b,a,c))
            m.addAction(action)
        m.exec_(self.cards.mapToGlobal(QPoint(0,0)))

    def cardChangeTriggered(self, bool, action, card):
        model = self.deck.currentModel
        if bool:
            card.active = True
            self.deck.currentModel.cardModels.remove(card)
            self.deck.currentModel.cardModels.append(card)
        else:
            active = 0
            for c in model.cardModels:
                if c.active:
                    active += 1
            if active > 1:
                card.active = False
        self.drawCardModels()

class AddModel(QDialog):

    def __init__(self, parent, main=None, online=False):
        QDialog.__init__(self, parent)
        self.parent = parent
        if not main:
            main = parent
        self.main = main
        self.model = None
        self.dialog = ankiqt.forms.addmodel.Ui_AddModel()
        self.dialog.setupUi(self)
        self.models = {}
        for name in (
            "Japanese",
            "English",
            "Cantonese",
            "Mandarin",
            "Heisig"):
            # hard code the order so that most common come first
            m = stdmodels.byName(name)
            item = QListWidgetItem(m.name)
            self.dialog.models.addItem(item)
            self.models[m.name] = m
        self.dialog.models.setCurrentRow(0)
        # the list widget will swallow the enter key
        s = QShortcut(QKeySequence("Return"), self)
        self.connect(s, SIGNAL("activated()"), self.accept)
        if not online:
            self.dialog.loadOnline.setShown(False)

    def getModel(self):
        self.exec_()
        return self.model

    def accept(self):
        if self.dialog.createTemplate.isChecked():
            self.model = self.models[
                unicode(self.dialog.models.currentItem().text())]
        elif self.dialog.createBasic.isChecked():
            self.model = stdmodels.byName("Basic")
        else:
            self.model = "online"
        QDialog.accept(self)

