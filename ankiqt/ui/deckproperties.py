# Copyright: Damien Elmes <anki@ichi2.net>
# License: GNU GPL, version 2 or later; http://www.gnu.org/copyleft/gpl.html

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys, re
import ankiqt.forms
import anki
from ankiqt import ui
from anki.utils import parseTags
from anki.deck import NewCardOrder

#         self.dialog.cardPos.clear()
#         self.dialog.cardPos.insertItems(
#             0, QStringList(Positions.values()))
#         self.dialog.cardPos.setCurrentIndex(self.m.position)


class DeckProperties(QDialog):

    def __init__(self, parent):
        QDialog.__init__(self, parent, Qt.Window)
        self.parent = parent
        self.d = parent.deck
        self.origMod = self.d.modified
        self.alreadyClosed = False
        self.dialog = ankiqt.forms.deckproperties.Ui_DeckProperties()
        self.dialog.setupUi(self)
        self.dialog.newCardOrder.insertItems(
            0, QStringList(NewCardOrder.values()))
        self.readData()
        self.connect(self.dialog.modelsAdd, SIGNAL("clicked()"), self.onAdd)
        self.connect(self.dialog.modelsEdit, SIGNAL("clicked()"), self.onEdit)
        self.connect(self.dialog.modelsDelete, SIGNAL("clicked()"), self.onDelete)
        self.show()

    def readData(self):
        # description
        self.dialog.deckDescription.setText(self.d.description)
        # syncing
        sn = self.d.syncName
        if sn:
            self.dialog.doSync.setCheckState(Qt.Checked)
            self.dialog.syncName.setText(sn)
        else:
            self.dialog.doSync.setCheckState(Qt.Unchecked)
            self.dialog.syncName.setText(self.d.name())
        # priorities
        self.dialog.highPriority.setText(self.d.highPriority)
        self.dialog.medPriority.setText(self.d.medPriority)
        self.dialog.lowPriority.setText(self.d.lowPriority)
        self.dialog.postponing.setText(self.d.suspended)
        # scheduling
        for type in ("hard", "mid", "easy"):
            v = getattr(self.d, type + "IntervalMin")
            getattr(self.dialog, type + "Min").setText("%0.1f" % v)
            v = getattr(self.d, type + "IntervalMax")
            getattr(self.dialog, type + "Max").setText("%0.1f" % v)
        self.dialog.delay0.setText(unicode(self.d.delay0/60.0))
        self.dialog.delay1.setText(unicode(self.d.delay1/60.0))
        self.dialog.delay2.setText(unicode(self.d.delay2/60.0))
        self.dialog.collapse.setText(unicode(self.d.collapseTime/60.0/60.0))
        self.dialog.failedCardMax.setText(unicode(self.d.failedCardMax))
        self.dialog.newCardOrder.setCurrentIndex(self.d.newCardOrder)
        # models
        self.updateModelsList()

    def updateModelsList(self):
        self.dialog.modelsList.clear()
        self.models = {}
        for model in self.d.models:
            name = _("%(name)s [%(facts)d facts]") % {
                'name': model.name,
                'facts': self.d.modelUseCount(model),
                }
            self.models[name] = model
        for (name, model) in sorted(self.models.items()):
            item = QListWidgetItem(name)
            self.dialog.modelsList.addItem(item)
            if model == self.d.currentModel:
                self.dialog.modelsList.setCurrentItem(item)

    def onAdd(self):
        m = ui.modelchooser.AddModel(self, self.parent).getModel()
        if m:
            self.d.addModel(m)
            self.updateModelsList()

    def onEdit(self):
        model = self.selectedModel()
        if not model:
            return
        ui.modelproperties.ModelProperties(self, model, self.parent)
        self.updateModelsList()

    def onDelete(self):
        model = self.selectedModel()
        row = self.dialog.modelsList.currentRow()
        if not model:
            return
        if len(self.d.models) < 2:
            ui.utils.showWarning(_("Please add another model first."),
                                 parent=self)
            return
        count = self.d.modelUseCount(model)
        if count:
            if not ui.utils.askUser(
                _("This model is used by %d facts.\n"
                  "Are you sure you want to delete it?\n"
                  "If you delete it, these cards will be lost.")
                % count, parent=self):
                return
        self.d.deleteModel(model)
        self.updateModelsList()
        self.dialog.modelsList.setCurrentRow(row)

    def selectedModel(self):
        row = self.dialog.modelsList.currentRow()
        if row == -1:
            return None
        return sorted(self.models.items())[self.dialog.modelsList.currentRow()][1]

    def updateField(self, obj, field, value):
        if getattr(obj, field) != value:
            setattr(obj, field, value)
            self.d.setModified()

    def reject(self):
        if self.alreadyClosed:
            return
        # description
        self.updateField(self.d, 'description',
                         unicode(self.dialog.deckDescription.toPlainText()))
        # syncing
        if self.dialog.doSync.checkState() == Qt.Checked:
            self.updateField(self.d, 'syncName',
                             unicode(self.dialog.syncName.text()))
        else:
            self.updateField(self.d, 'syncName', None)
        # scheduling
        minmax = ("Min", "Max")
        for type in ("hard", "mid", "easy"):
            v = getattr(self.dialog, type + "Min").text()
            try:
                v = float(v)
            except ValueError:
                continue
            self.updateField(self.d, type + "IntervalMin", v)
            v = getattr(self.dialog, type + "Max").text()
            try:
                v = float(v)
            except ValueError:
                continue
            self.updateField(self.d, type + "IntervalMax", v)
        try:
            v = float(self.dialog.delay0.text()) * 60.0
            self.updateField(self.d, 'delay0', v)
            v = float(self.dialog.delay1.text()) * 60.0
            self.updateField(self.d, 'delay1', v)
            v = float(self.dialog.delay2.text()) * 60.0
            self.updateField(self.d, 'delay2', v)
            v = float(self.dialog.collapse.text()) * 60.0 * 60.0
            self.updateField(self.d, 'collapseTime', v)
            v = int(self.dialog.failedCardMax.text())
            self.updateField(self.d, 'failedCardMax', v)
        except ValueError:
            pass
        self.updateField(self.d,
                         "highPriority",
                         unicode(self.dialog.highPriority.text()))
        self.updateField(self.d,
                         "medPriority",
                         unicode(self.dialog.medPriority.text()))
        self.updateField(self.d,
                         "lowPriority",
                         unicode(self.dialog.lowPriority.text()))
        self.updateField(self.d,
                         "suspended",
                         unicode(self.dialog.postponing.text()))
        # new card order
        self.updateField(self.d, "newCardOrder",
                         self.dialog.newCardOrder.currentIndex())
        # mark deck dirty and close
        self.alreadyClosed = True
        self.close()
        if self.origMod != self.d.modified:
            self.parent.reset()