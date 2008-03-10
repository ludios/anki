# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/cardlist.ui'
#

#      by: PyQt4 UI code generator 4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_EditDeck(object):
    def setupUi(self, EditDeck):
        EditDeck.setObjectName("EditDeck")
        EditDeck.setWindowModality(QtCore.Qt.NonModal)
        EditDeck.resize(QtCore.QSize(QtCore.QRect(0,0,710,655).size()).expandedTo(EditDeck.minimumSizeHint()))
        EditDeck.setWindowIcon(QtGui.QIcon(":/icons/view_text.png"))

        self.vboxlayout = QtGui.QVBoxLayout(EditDeck)
        self.vboxlayout.setSpacing(3)
        self.vboxlayout.setMargin(3)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setObjectName("hboxlayout")

        self.searchGroup = QtGui.QGroupBox(EditDeck)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchGroup.sizePolicy().hasHeightForWidth())
        self.searchGroup.setSizePolicy(sizePolicy)
        self.searchGroup.setMinimumSize(QtCore.QSize(400,0))
        self.searchGroup.setObjectName("searchGroup")

        self.hboxlayout1 = QtGui.QHBoxLayout(self.searchGroup)
        self.hboxlayout1.setSpacing(3)
        self.hboxlayout1.setMargin(3)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.filterEdit = QtGui.QLineEdit(self.searchGroup)
        self.filterEdit.setObjectName("filterEdit")
        self.hboxlayout1.addWidget(self.filterEdit)

        self.tagList = QtGui.QComboBox(self.searchGroup)
        self.tagList.setMinimumSize(QtCore.QSize(150,0))
        self.tagList.setObjectName("tagList")
        self.hboxlayout1.addWidget(self.tagList)
        self.hboxlayout.addWidget(self.searchGroup)

        self.sortGroup = QtGui.QGroupBox(EditDeck)
        self.sortGroup.setObjectName("sortGroup")

        self.hboxlayout2 = QtGui.QHBoxLayout(self.sortGroup)
        self.hboxlayout2.setSpacing(3)
        self.hboxlayout2.setMargin(3)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.sortBox = QtGui.QComboBox(self.sortGroup)
        self.sortBox.setObjectName("sortBox")
        self.hboxlayout2.addWidget(self.sortBox)
        self.hboxlayout.addWidget(self.sortGroup)

        self.groupBox = QtGui.QGroupBox(EditDeck)
        self.groupBox.setObjectName("groupBox")

        self.hboxlayout3 = QtGui.QHBoxLayout(self.groupBox)
        self.hboxlayout3.setSpacing(3)
        self.hboxlayout3.setMargin(3)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.factsButton = QtGui.QPushButton(self.groupBox)
        self.factsButton.setIcon(QtGui.QIcon(":/icons/Anki_Fact.png"))
        self.factsButton.setAutoDefault(False)
        self.factsButton.setObjectName("factsButton")
        self.hboxlayout3.addWidget(self.factsButton)

        self.cardsButton = QtGui.QPushButton(self.groupBox)
        self.cardsButton.setIcon(QtGui.QIcon(":/icons/Anki_Card.png"))
        self.cardsButton.setAutoDefault(False)
        self.cardsButton.setObjectName("cardsButton")
        self.hboxlayout3.addWidget(self.cardsButton)
        self.hboxlayout.addWidget(self.groupBox)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.splitter = QtGui.QSplitter(EditDeck)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")

        self.tableView = QtGui.QTableView(self.splitter)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tableView.setFrameShape(QtGui.QFrame.NoFrame)
        self.tableView.setFrameShadow(QtGui.QFrame.Plain)
        self.tableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableView.setTabKeyNavigation(False)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")

        self.frame = QtGui.QFrame(self.splitter)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.frame)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.cardInfoGroup = QtGui.QGroupBox(self.frame)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.cardInfoGroup.sizePolicy().hasHeightForWidth())
        self.cardInfoGroup.setSizePolicy(sizePolicy)
        self.cardInfoGroup.setMinimumSize(QtCore.QSize(0,300))
        self.cardInfoGroup.setObjectName("cardInfoGroup")
        self.gridlayout.addWidget(self.cardInfoGroup,0,1,1,1)

        self.fieldsArea = QtGui.QGroupBox(self.frame)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.fieldsArea.sizePolicy().hasHeightForWidth())
        self.fieldsArea.setSizePolicy(sizePolicy)
        self.fieldsArea.setObjectName("fieldsArea")
        self.gridlayout.addWidget(self.fieldsArea,0,0,1,1)
        self.vboxlayout1.addLayout(self.gridlayout)
        self.vboxlayout.addWidget(self.splitter)

        self.action_Delete_card = QtGui.QAction(EditDeck)
        self.action_Delete_card.setIcon(QtGui.QIcon(":/icons/editdelete.png"))
        self.action_Delete_card.setObjectName("action_Delete_card")

        self.actionAdd_fact_tag = QtGui.QAction(EditDeck)
        self.actionAdd_fact_tag.setIcon(QtGui.QIcon(":/icons/Anki_Add_Tag.png"))
        self.actionAdd_fact_tag.setObjectName("actionAdd_fact_tag")

        self.actionAdd_card_tag = QtGui.QAction(EditDeck)
        self.actionAdd_card_tag.setIcon(QtGui.QIcon(":/icons/Anki_Add_Tag.png"))
        self.actionAdd_card_tag.setObjectName("actionAdd_card_tag")

        self.actionDelete_fact_tag = QtGui.QAction(EditDeck)
        self.actionDelete_fact_tag.setIcon(QtGui.QIcon(":/icons/Anki_Del_Tag.png"))
        self.actionDelete_fact_tag.setObjectName("actionDelete_fact_tag")

        self.actionDelete_card_tag = QtGui.QAction(EditDeck)
        self.actionDelete_card_tag.setIcon(QtGui.QIcon(":/icons/Anki_Del_Tag.png"))
        self.actionDelete_card_tag.setObjectName("actionDelete_card_tag")

        self.actionAdd_Missing_Cards = QtGui.QAction(EditDeck)
        self.actionAdd_Missing_Cards.setIcon(QtGui.QIcon(":/icons/Anki_Card.png"))
        self.actionAdd_Missing_Cards.setObjectName("actionAdd_Missing_Cards")

        self.actionDelete_Fact = QtGui.QAction(EditDeck)
        self.actionDelete_Fact.setIcon(QtGui.QIcon(":/icons/editdelete.png"))
        self.actionDelete_Fact.setObjectName("actionDelete_Fact")

        self.actionResetCardProgress = QtGui.QAction(EditDeck)
        self.actionResetCardProgress.setObjectName("actionResetCardProgress")

        self.actionResetFactProgress = QtGui.QAction(EditDeck)
        self.actionResetFactProgress.setObjectName("actionResetFactProgress")

        self.retranslateUi(EditDeck)
        QtCore.QMetaObject.connectSlotsByName(EditDeck)

    def retranslateUi(self, EditDeck):
        EditDeck.setWindowTitle(_("Anki - Edit Deck"))
        self.searchGroup.setTitle(_("&Search"))
        self.sortGroup.setTitle(_("S&ort"))
        self.groupBox.setTitle(_("Actions on selected.."))
        self.factsButton.setText(_("Facts.."))
        self.cardsButton.setText(_("Cards.."))
        self.cardInfoGroup.setTitle(_("Current Card"))
        self.fieldsArea.setTitle(_("Current &Fact"))
        self.action_Delete_card.setText(_("Toggle Delete"))
        self.actionAdd_fact_tag.setText(_("Add Tag.."))
        self.actionAdd_card_tag.setText(_("Add Tag.."))
        self.actionDelete_fact_tag.setText(_("Delete Tag.."))
        self.actionDelete_card_tag.setText(_("Delete Tag.."))
        self.actionAdd_Missing_Cards.setText(_("Add Missing Active Cards"))
        self.actionDelete_Fact.setText(_("Toggle Delete"))
        self.actionResetCardProgress.setText(_("Reset Progress"))
        self.actionResetFactProgress.setText(_("Reset Progress"))

import icons_rc
