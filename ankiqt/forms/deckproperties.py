# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/deckproperties.ui'
#

#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DeckProperties(object):
    def setupUi(self, DeckProperties):
        DeckProperties.setObjectName("DeckProperties")
        DeckProperties.setWindowModality(QtCore.Qt.ApplicationModal)
        DeckProperties.resize(QtCore.QSize(QtCore.QRect(0,0,491,535).size()).expandedTo(DeckProperties.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(DeckProperties)
        self.vboxlayout.setObjectName("vboxlayout")

        self.qtabwidget = QtGui.QTabWidget(DeckProperties)
        self.qtabwidget.setObjectName("qtabwidget")

        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.tab)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setMargin(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName("label")
        self.vboxlayout1.addWidget(self.label)

        self.deckDescription = QtGui.QTextEdit(self.tab)
        self.deckDescription.setMinimumSize(QtCore.QSize(0,100))
        self.deckDescription.setTabChangesFocus(True)
        self.deckDescription.setObjectName("deckDescription")
        self.vboxlayout1.addWidget(self.deckDescription)

        self.label_13 = QtGui.QLabel(self.tab)
        self.label_13.setScaledContents(False)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.vboxlayout1.addWidget(self.label_13)

        self.doSync = QtGui.QCheckBox(self.tab)
        self.doSync.setObjectName("doSync")
        self.vboxlayout1.addWidget(self.doSync)

        self.syncName = QtGui.QLineEdit(self.tab)
        self.syncName.setEnabled(False)
        self.syncName.setObjectName("syncName")
        self.vboxlayout1.addWidget(self.syncName)
        self.qtabwidget.addTab(self.tab,"")

        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")

        self.vboxlayout2 = QtGui.QVBoxLayout(self.tab_4)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setMargin(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.label_21 = QtGui.QLabel(self.tab_4)
        self.label_21.setWordWrap(True)
        self.label_21.setObjectName("label_21")
        self.vboxlayout2.addWidget(self.label_21)

        self.highPriority = QtGui.QLineEdit(self.tab_4)
        self.highPriority.setObjectName("highPriority")
        self.vboxlayout2.addWidget(self.highPriority)

        self.label_17 = QtGui.QLabel(self.tab_4)
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.vboxlayout2.addWidget(self.label_17)

        self.medPriority = QtGui.QLineEdit(self.tab_4)
        self.medPriority.setObjectName("medPriority")
        self.vboxlayout2.addWidget(self.medPriority)

        self.label_24 = QtGui.QLabel(self.tab_4)
        self.label_24.setWordWrap(True)
        self.label_24.setObjectName("label_24")
        self.vboxlayout2.addWidget(self.label_24)

        self.lowPriority = QtGui.QLineEdit(self.tab_4)
        self.lowPriority.setObjectName("lowPriority")
        self.vboxlayout2.addWidget(self.lowPriority)

        self.label_23 = QtGui.QLabel(self.tab_4)
        self.label_23.setWordWrap(True)
        self.label_23.setObjectName("label_23")
        self.vboxlayout2.addWidget(self.label_23)

        self.postponing = QtGui.QLineEdit(self.tab_4)
        self.postponing.setObjectName("postponing")
        self.vboxlayout2.addWidget(self.postponing)

        spacerItem = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout2.addItem(spacerItem)
        self.qtabwidget.addTab(self.tab_4,"")

        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.tab_2)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setMargin(6)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.label_15 = QtGui.QLabel(self.tab_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.vboxlayout3.addWidget(self.label_15)

        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setMinimumSize(QtCore.QSize(220,0))
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2,0,0,1,1)

        self.easyMin = QtGui.QLineEdit(self.tab_2)
        self.easyMin.setObjectName("easyMin")
        self.gridlayout.addWidget(self.easyMin,2,2,1,1)

        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.gridlayout.addWidget(self.label_6,1,1,1,1)

        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.gridlayout.addWidget(self.label_7,2,1,1,1)

        self.midMax = QtGui.QLineEdit(self.tab_2)
        self.midMax.setObjectName("midMax")
        self.gridlayout.addWidget(self.midMax,1,4,1,1)

        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4,2,0,1,1)

        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3,1,0,1,1)

        self.label_10 = QtGui.QLabel(self.tab_2)
        self.label_10.setObjectName("label_10")
        self.gridlayout.addWidget(self.label_10,2,3,1,1)

        self.hardMin = QtGui.QLineEdit(self.tab_2)
        self.hardMin.setObjectName("hardMin")
        self.gridlayout.addWidget(self.hardMin,0,2,1,1)

        self.midMin = QtGui.QLineEdit(self.tab_2)
        self.midMin.setObjectName("midMin")
        self.gridlayout.addWidget(self.midMin,1,2,1,1)

        self.label_8 = QtGui.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.gridlayout.addWidget(self.label_8,0,3,1,1)

        self.easyMax = QtGui.QLineEdit(self.tab_2)
        self.easyMax.setObjectName("easyMax")
        self.gridlayout.addWidget(self.easyMax,2,4,1,1)

        self.hardMax = QtGui.QLineEdit(self.tab_2)
        self.hardMax.setObjectName("hardMax")
        self.gridlayout.addWidget(self.hardMax,0,4,1,1)

        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5,0,1,1,1)

        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.gridlayout.addWidget(self.label_9,1,3,1,1)
        self.vboxlayout3.addLayout(self.gridlayout)

        self.label_11 = QtGui.QLabel(self.tab_2)
        self.label_11.setObjectName("label_11")
        self.vboxlayout3.addWidget(self.label_11)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.newCardOrder = QtGui.QComboBox(self.tab_2)
        self.newCardOrder.setObjectName("newCardOrder")
        self.hboxlayout.addWidget(self.newCardOrder)

        spacerItem1 = QtGui.QSpacerItem(180,20,QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.vboxlayout3.addLayout(self.hboxlayout)

        self.label_18 = QtGui.QLabel(self.tab_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setObjectName("label_18")
        self.vboxlayout3.addWidget(self.label_18)

        self.gridlayout1 = QtGui.QGridLayout()
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")

        self.label_20 = QtGui.QLabel(self.tab_2)
        self.label_20.setObjectName("label_20")
        self.gridlayout1.addWidget(self.label_20,0,0,1,1)

        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout1.addItem(spacerItem2,0,1,1,1)

        self.label_22 = QtGui.QLabel(self.tab_2)
        self.label_22.setObjectName("label_22")
        self.gridlayout1.addWidget(self.label_22,1,0,1,1)

        spacerItem3 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout1.addItem(spacerItem3,1,1,1,1)

        self.delay0 = QtGui.QLineEdit(self.tab_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delay0.sizePolicy().hasHeightForWidth())
        self.delay0.setSizePolicy(sizePolicy)
        self.delay0.setObjectName("delay0")
        self.gridlayout1.addWidget(self.delay0,0,2,1,1)

        self.delay1 = QtGui.QLineEdit(self.tab_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delay1.sizePolicy().hasHeightForWidth())
        self.delay1.setSizePolicy(sizePolicy)
        self.delay1.setObjectName("delay1")
        self.gridlayout1.addWidget(self.delay1,1,2,1,1)

        self.label_19 = QtGui.QLabel(self.tab_2)
        self.label_19.setObjectName("label_19")
        self.gridlayout1.addWidget(self.label_19,2,0,1,1)

        spacerItem4 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout1.addItem(spacerItem4,2,1,1,1)

        self.delay2 = QtGui.QLineEdit(self.tab_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delay2.sizePolicy().hasHeightForWidth())
        self.delay2.setSizePolicy(sizePolicy)
        self.delay2.setObjectName("delay2")
        self.gridlayout1.addWidget(self.delay2,2,2,1,1)
        self.vboxlayout3.addLayout(self.gridlayout1)

        self.label_25 = QtGui.QLabel(self.tab_2)
        self.label_25.setObjectName("label_25")
        self.vboxlayout3.addWidget(self.label_25)

        self.gridlayout2 = QtGui.QGridLayout()
        self.gridlayout2.setObjectName("gridlayout2")

        self.label_26 = QtGui.QLabel(self.tab_2)
        self.label_26.setObjectName("label_26")
        self.gridlayout2.addWidget(self.label_26,0,0,1,1)

        spacerItem5 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout2.addItem(spacerItem5,0,1,1,1)

        self.collapse = QtGui.QLineEdit(self.tab_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.collapse.sizePolicy().hasHeightForWidth())
        self.collapse.setSizePolicy(sizePolicy)
        self.collapse.setObjectName("collapse")
        self.gridlayout2.addWidget(self.collapse,0,2,1,1)

        self.label_12 = QtGui.QLabel(self.tab_2)
        self.label_12.setObjectName("label_12")
        self.gridlayout2.addWidget(self.label_12,1,0,1,1)

        self.failedCardMax = QtGui.QLineEdit(self.tab_2)
        self.failedCardMax.setObjectName("failedCardMax")
        self.gridlayout2.addWidget(self.failedCardMax,1,2,1,1)
        self.vboxlayout3.addLayout(self.gridlayout2)

        spacerItem6 = QtGui.QSpacerItem(20,20,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Preferred)
        self.vboxlayout3.addItem(spacerItem6)
        self.qtabwidget.addTab(self.tab_2,"")

        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")

        self.vboxlayout4 = QtGui.QVBoxLayout(self.tab_3)
        self.vboxlayout4.setSpacing(6)
        self.vboxlayout4.setMargin(6)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.label_14 = QtGui.QLabel(self.tab_3)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.vboxlayout4.addWidget(self.label_14)

        self.modelsList = QtGui.QListWidget(self.tab_3)
        self.modelsList.setObjectName("modelsList")
        self.vboxlayout4.addWidget(self.modelsList)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.modelsAdd = QtGui.QPushButton(self.tab_3)
        self.modelsAdd.setObjectName("modelsAdd")
        self.hboxlayout1.addWidget(self.modelsAdd)

        self.modelsEdit = QtGui.QPushButton(self.tab_3)
        self.modelsEdit.setObjectName("modelsEdit")
        self.hboxlayout1.addWidget(self.modelsEdit)

        self.modelsDelete = QtGui.QPushButton(self.tab_3)
        self.modelsDelete.setObjectName("modelsDelete")
        self.hboxlayout1.addWidget(self.modelsDelete)
        self.vboxlayout4.addLayout(self.hboxlayout1)
        self.qtabwidget.addTab(self.tab_3,"")
        self.vboxlayout.addWidget(self.qtabwidget)

        self.buttonBox = QtGui.QDialogButtonBox(DeckProperties)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(DeckProperties)
        self.qtabwidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),DeckProperties.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),DeckProperties.reject)
        QtCore.QObject.connect(self.doSync,QtCore.SIGNAL("toggled(bool)"),self.syncName.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(DeckProperties)
        DeckProperties.setTabOrder(self.qtabwidget,self.deckDescription)
        DeckProperties.setTabOrder(self.deckDescription,self.doSync)
        DeckProperties.setTabOrder(self.doSync,self.syncName)
        DeckProperties.setTabOrder(self.syncName,self.highPriority)
        DeckProperties.setTabOrder(self.highPriority,self.medPriority)
        DeckProperties.setTabOrder(self.medPriority,self.lowPriority)
        DeckProperties.setTabOrder(self.lowPriority,self.postponing)
        DeckProperties.setTabOrder(self.postponing,self.hardMin)
        DeckProperties.setTabOrder(self.hardMin,self.hardMax)
        DeckProperties.setTabOrder(self.hardMax,self.midMin)
        DeckProperties.setTabOrder(self.midMin,self.midMax)
        DeckProperties.setTabOrder(self.midMax,self.easyMin)
        DeckProperties.setTabOrder(self.easyMin,self.easyMax)
        DeckProperties.setTabOrder(self.easyMax,self.newCardOrder)
        DeckProperties.setTabOrder(self.newCardOrder,self.delay0)
        DeckProperties.setTabOrder(self.delay0,self.delay1)
        DeckProperties.setTabOrder(self.delay1,self.delay2)
        DeckProperties.setTabOrder(self.delay2,self.collapse)
        DeckProperties.setTabOrder(self.collapse,self.failedCardMax)
        DeckProperties.setTabOrder(self.failedCardMax,self.modelsList)
        DeckProperties.setTabOrder(self.modelsList,self.modelsAdd)
        DeckProperties.setTabOrder(self.modelsAdd,self.modelsEdit)
        DeckProperties.setTabOrder(self.modelsEdit,self.modelsDelete)
        DeckProperties.setTabOrder(self.modelsDelete,self.buttonBox)

    def retranslateUi(self, DeckProperties):
        DeckProperties.setWindowTitle(_("Edit deck properties"))
        self.label.setText(_("<h1>Deck description</h1>"))
        self.label_13.setText(_("<h1>Synchronisation</h1>Synchronisation lets you use your deck on multiple computers at the same time. You can also use it to study on the web, for when you\'re not at home. You can also study on your mobile phone if your phone has internet access."))
        self.doSync.setText(_("Synchronize this deck with name:"))
        self.qtabwidget.setTabText(self.qtabwidget.indexOf(self.tab), _("Description && Synchronisation"))
        self.label_21.setText(_("<h1>Very high priority</h1>A comma-separated list of tags to prioritize. Matching cards are placed at the top of the revision queue."))
        self.label_17.setText(_("<h1>High priority</h1>Matching cards are placed at the top of the revision queue or new card queue, depending on if they have been seen before."))
        self.label_24.setText(_("<h1>Low priority</h1>Matching cards are placed at the bottom of the new card queue."))
        self.label_23.setText(_("<h1>Postponing</h1>Any matching cards will not be shown until unsuspended. The web and phone interfaces automatically add \'noweb\' and \'nophone\' - give these tags to your cards to prevent them from showing on the phone or web interface."))
        self.qtabwidget.setTabText(self.qtabwidget.indexOf(self.tab_4), _("Priorities && Postponing"))
        self.label_15.setText(_("<h1>New & young cards</h1>The initial times to use when scheduling cards, in days."))
        self.label_2.setText(_("<b>Hard</b>"))
        self.label_6.setText(_("Min"))
        self.label_7.setText(_("Min"))
        self.label_4.setText(_("<b>Easy</b>"))
        self.label_3.setText(_("<b>Medium</b>"))
        self.label_10.setText(_("Max"))
        self.label_8.setText(_("Max"))
        self.label_5.setText(_("Min"))
        self.label_9.setText(_("Max"))
        self.label_11.setText(_("The order to show new cards."))
        self.label_18.setText(_("<h1>Delay on mistake</h1>The time until Anki shows you a card you got wrong. The default is 10 minutes."))
        self.label_20.setText(_("<b>Totally forgot (0)</b>"))
        self.label_22.setText(_("<b>Made a mistake (1) on a young card"))
        self.label_19.setText(_("<b>Made a mistake (1) on a mature card</b>"))
        self.label_25.setText(_("<h1>Final drill & failed card limit</h1>"))
        self.label_26.setText(_("The number of hours to collapse in the final drill. Use 0 to disable."))
        self.label_12.setText(_("The maximum number of failed cards to allow at once."))
        self.qtabwidget.setTabText(self.qtabwidget.indexOf(self.tab_2), _("Scheduling"))
        self.label_14.setText(_("<h1>Models</h1>Models define what sort of information you\'re studying, and the way to show it to you. Models range from a simple representation of a single flashcard with a \"front\" and \"back\" side, to more complicated domain specific models: a model for Russian verbs may define two verb forms, and test you on both of them."))
        self.modelsAdd.setText(_("&Add"))
        self.modelsEdit.setText(_("&Edit"))
        self.modelsDelete.setText(_("&Delete"))
        self.qtabwidget.setTabText(self.qtabwidget.indexOf(self.tab_3), _("Models"))

