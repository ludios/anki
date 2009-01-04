# Copyright: Damien Elmes <anki@ichi2.net>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys, re, time
import ankiqt.forms
import anki
from ankiqt import ui
from anki.utils import parseTags
from anki.deck import newCardOrderLabels, newCardSchedulingLabels
from anki.deck import revCardOrderLabels
from anki.utils import hexifyID, dehexifyID
from anki.lang import ngettext

tabs = ("Scheduling",
        "Synchronization",
        "Models",
        "Advanced")

class DeckProperties(QDialog):

    def __init__(self, parent):
        QDialog.__init__(self, parent, Qt.Window)
        self.parent = parent
        self.d = parent.deck
        self.origMod = self.d.modified
        self.dialog = ankiqt.forms.deckproperties.Ui_DeckProperties()
        self.dialog.setupUi(self)
        self.dialog.newCardOrder.insertItems(
            0, QStringList(newCardOrderLabels().values()))
        self.dialog.newCardScheduling.insertItems(
            0, QStringList(newCardSchedulingLabels().values()))
        self.dialog.revCardOrder.insertItems(
            0, QStringList(revCardOrderLabels().values()))
        self.readData()
        self.connect(self.dialog.modelsAdd, SIGNAL("clicked()"), self.onAdd)
        self.connect(self.dialog.modelsEdit, SIGNAL("clicked()"), self.onEdit)
        self.connect(self.dialog.modelsDelete, SIGNAL("clicked()"), self.onDelete)
        self.connect(self.dialog.buttonBox, SIGNAL("helpRequested()"), self.helpRequested)
        self.connect(self.dialog.addSource, SIGNAL("clicked()"), self.onAddSource)
        self.connect(self.dialog.deleteSource, SIGNAL("clicked()"), self.onDeleteSource)

        self.show()

    def readData(self):
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
            getattr(self.dialog, type + "Min").setText("%0.3f" % v)
            v = getattr(self.d, type + "IntervalMax")
            getattr(self.dialog, type + "Max").setText("%0.3f" % v)
        self.dialog.delay0.setText(unicode(self.d.delay0/60.0))
        self.dialog.delay1.setText(unicode(self.d.delay1/60.0))
        self.dialog.delay2.setText(unicode(self.d.delay2))
        self.dialog.collapse.setCheckState(self.d.collapseTime
                                           and Qt.Checked or Qt.Unchecked)
        self.dialog.failedCardMax.setText(unicode(self.d.failedCardMax))
        self.dialog.newCardsPerDay.setText(unicode(self.d.newCardsPerDay))
        self.dialog.newCardOrder.setCurrentIndex(self.d.newCardOrder)
        self.dialog.newCardScheduling.setCurrentIndex(self.d.newCardSpacing)
        self.dialog.revCardOrder.setCurrentIndex(self.d.revCardOrder)
        # sources
        self.sources = self.d.s.all("select id, name from sources")
        self.sourcesToRemove = []
        self.drawSourcesTable()
        # models
        self.updateModelsList()
        # hour shift
        self.dialog.timeOffset.setText(str(
            (self.d.utcOffset - time.timezone) / 60.0 / 60.0))

    def drawSourcesTable(self):
        self.dialog.sourcesTable.clear()
        self.dialog.sourcesTable.setRowCount(len(self.sources))
        self.dialog.sourcesTable.setColumnCount(2)
        self.dialog.sourcesTable.setHorizontalHeaderLabels(
            QStringList([_("ID"),
                         _("Name")]))
        self.dialog.sourcesTable.horizontalHeader().setResizeMode(
            QHeaderView.Stretch)
        self.dialog.sourcesTable.verticalHeader().hide()
        self.dialog.sourcesTable.setSelectionBehavior(
            QAbstractItemView.SelectRows)
        self.dialog.sourcesTable.setSelectionMode(
            QAbstractItemView.SingleSelection)
        self.sourceItems = []
        n = 0
        for (id, name) in self.sources:
            a = QTableWidgetItem(hexifyID(id))
            b = QTableWidgetItem(name)
            self.sourceItems.append([a, b])
            self.dialog.sourcesTable.setItem(n, 0, a)
            self.dialog.sourcesTable.setItem(n, 1, b)
            n += 1

    def updateModelsList(self):
        idx = self.dialog.modelsList.currentRow()
        self.dialog.modelsList.clear()
        self.models = []
        for model in self.d.models:
            name = ngettext("%(name)s [%(facts)d fact]",
                "%(name)s [%(facts)d facts]", self.d.modelUseCount(model)) % {
                    'name': model.name,
                    'facts': self.d.modelUseCount(model),
                }
            self.models.append((name, model))
        self.models.sort()
        for (name, model) in self.models:
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
        # set to current
        self.d.currentModel = model
        ui.modelproperties.ModelProperties(self, model, self.parent, onFinish=
                                           self.updateModelsList)

    def onDelete(self):
        model = self.selectedModel()
        row = self.dialog.modelsList.currentRow()
        if not model:
            return
        if len(self.d.models) < 2:
            ui.utils.showWarning(_("Please add another model first."),
                                 parent=self)
            return
        if self.d.s.scalar("select 1 from sources where id=:id",
                           id=model.source):
            ui.utils.showWarning(_("This model is used by deck source:\n"
                                   "%s\nYou will need to remove the source "
                                   "first.") % hexifyID(model.source))
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
        return self.models[self.dialog.modelsList.currentRow()][1]

    def updateField(self, obj, field, value):
        if getattr(obj, field) != value:
            setattr(obj, field, value)
            self.d.setModified()

    def helpRequested(self):
        idx = self.dialog.qtabwidget.currentIndex()
        QDesktopServices.openUrl(QUrl(ankiqt.appWiki +
                                      "DeckProperties#" +
                                      tabs[idx]))

    def onAddSource(self):
        (s, ret) = QInputDialog.getText(self, _("Anki"),
                                        _("Source ID:"))
        if not s:
            return
        rc = self.dialog.sourcesTable.rowCount()
        self.dialog.sourcesTable.insertRow(rc)
        a = QTableWidgetItem(s)
        b = QTableWidgetItem("")
        self.dialog.sourcesTable.setItem(rc, 0, a)
        self.dialog.sourcesTable.setItem(rc, 1, b)

    def onDeleteSource(self):
        r = self.dialog.sourcesTable.currentRow()
        if r == -1:
            return
        self.dialog.sourcesTable.removeRow(r)
        try:
            id = self.sources[r][0]
            self.sourcesToRemove.append(id)
        except IndexError:
            pass

    def reject(self):
        n = _("Deck Properties")
        self.parent.deck.setUndoStart(n)
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
            v = float(self.dialog.delay2.text())
            self.updateField(self.d, 'delay2', v)
            v = int(self.dialog.failedCardMax.text())
            self.updateField(self.d, 'failedCardMax', max(v, 5))
            v = int(self.dialog.newCardsPerDay.text())
            self.updateField(self.d, 'newCardsPerDay', v)
        except ValueError:
            pass
        # hour shift
        try:
            self.updateField(self.d, 'utcOffset',
                             float(str(self.dialog.timeOffset.text()))
                             *60*60 + time.timezone)
        except:
            pass
        self.updateField(self.d, 'collapseTime',
                         self.dialog.collapse.isChecked() and 1 or 0)
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
        self.updateField(self.d, "newCardSpacing",
                         self.dialog.newCardScheduling.currentIndex())
        self.updateField(self.d, "revCardOrder",
                         self.dialog.revCardOrder.currentIndex())
        # sources
        d = {}
        d.update(self.sources)
        for n in range(self.dialog.sourcesTable.rowCount()):
            try:
                id = dehexifyID(str(self.dialog.sourcesTable.item(n, 0).text()))
            except (ValueError,OverflowError):
                continue
            name = unicode(self.dialog.sourcesTable.item(n, 1).text())
            if id in d:
                if d[id] == name:
                    del d[id]
                    continue
                # name changed
                self.d.s.statement(
                    "update sources set name = :n where id = :id",
                    id=id, n=name)
            else:
                self.d.s.statement("""
insert into sources values
(:id, :n, :t, 0, 0)""", id=id, n=name, t=time.time())
            self.d.setModified()
            try:
                del d[id]
            except KeyError:
                pass
        for id in self.sourcesToRemove + d.keys():
            self.d.s.statement("delete from sources where id = :id",
                               id=id)
            self.d.setModified()
        # mark deck dirty and close
        if self.origMod != self.d.modified:
            self.parent.reset()
        self.parent.deck.setUndoEnd(n)
        QDialog.reject(self)
