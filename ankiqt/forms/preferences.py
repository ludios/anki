# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/preferences.ui'
#

#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        Preferences.setObjectName("Preferences")
        Preferences.resize(365, 467)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Preferences)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtGui.QTabWidget(Preferences)
        self.tabWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_1)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.tab_1)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.interfaceLang = QtGui.QComboBox(self.tab_1)
        self.interfaceLang.setMinimumSize(QtCore.QSize(300, 0))
        self.interfaceLang.setObjectName("interfaceLang")
        self.verticalLayout.addWidget(self.interfaceLang)
        self.label_2 = QtGui.QLabel(self.tab_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.showDivider = QtGui.QCheckBox(self.tab_1)
        self.showDivider.setObjectName("showDivider")
        self.verticalLayout.addWidget(self.showDivider)
        self.splitQA = QtGui.QCheckBox(self.tab_1)
        self.splitQA.setObjectName("splitQA")
        self.verticalLayout.addWidget(self.splitQA)
        self.showEstimates = QtGui.QCheckBox(self.tab_1)
        self.showEstimates.setObjectName("showEstimates")
        self.verticalLayout.addWidget(self.showEstimates)
        self.showProgress = QtGui.QCheckBox(self.tab_1)
        self.showProgress.setObjectName("showProgress")
        self.verticalLayout.addWidget(self.showProgress)
        self.preventEdits = QtGui.QCheckBox(self.tab_1)
        self.preventEdits.setObjectName("preventEdits")
        self.verticalLayout.addWidget(self.preventEdits)
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_3 = QtGui.QLabel(self.tab_1)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setSpacing(10)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setObjectName("hboxlayout")
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName("vboxlayout")
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.vboxlayout.addLayout(self.gridlayout)
        self.label_16 = QtGui.QLabel(self.tab_2)
        self.label_16.setWordWrap(True)
        self.label_16.setOpenExternalLinks(True)
        self.label_16.setObjectName("label_16")
        self.vboxlayout.addWidget(self.label_16)
        self.gridlayout1 = QtGui.QGridLayout()
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")
        self.label_18 = QtGui.QLabel(self.tab_2)
        self.label_18.setObjectName("label_18")
        self.gridlayout1.addWidget(self.label_18, 1, 0, 1, 1)
        self.label_17 = QtGui.QLabel(self.tab_2)
        self.label_17.setObjectName("label_17")
        self.gridlayout1.addWidget(self.label_17, 0, 0, 1, 1)
        self.syncUser = QtGui.QLineEdit(self.tab_2)
        self.syncUser.setObjectName("syncUser")
        self.gridlayout1.addWidget(self.syncUser, 0, 1, 1, 1)
        self.syncOnClose = QtGui.QCheckBox(self.tab_2)
        self.syncOnClose.setChecked(True)
        self.syncOnClose.setObjectName("syncOnClose")
        self.gridlayout1.addWidget(self.syncOnClose, 3, 0, 1, 1)
        self.syncPass = QtGui.QLineEdit(self.tab_2)
        self.syncPass.setEchoMode(QtGui.QLineEdit.Password)
        self.syncPass.setObjectName("syncPass")
        self.gridlayout1.addWidget(self.syncPass, 1, 1, 1, 1)
        self.syncOnOpen = QtGui.QCheckBox(self.tab_2)
        self.syncOnOpen.setChecked(True)
        self.syncOnOpen.setObjectName("syncOnOpen")
        self.gridlayout1.addWidget(self.syncOnOpen, 2, 0, 1, 1)
        self.syncOnProgramOpen = QtGui.QCheckBox(self.tab_2)
        self.syncOnProgramOpen.setObjectName("syncOnProgramOpen")
        self.gridlayout1.addWidget(self.syncOnProgramOpen, 4, 0, 1, 1)
        self.syncOnProgramClose = QtGui.QCheckBox(self.tab_2)
        self.syncOnProgramClose.setObjectName("syncOnProgramClose")
        self.gridlayout1.addWidget(self.syncOnProgramClose, 5, 0, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout1)
        self.hboxlayout.addLayout(self.vboxlayout)
        self.verticalLayout_4.addLayout(self.hboxlayout)
        self.label_13 = QtGui.QLabel(self.tab_2)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_4.addWidget(self.label_13)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setVerticalSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_14 = QtGui.QLabel(self.tab_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1)
        self.proxyHost = QtGui.QLineEdit(self.tab_2)
        self.proxyHost.setObjectName("proxyHost")
        self.gridLayout_3.addWidget(self.proxyHost, 0, 1, 1, 1)
        self.label_19 = QtGui.QLabel(self.tab_2)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 2, 0, 1, 1)
        self.proxyUser = QtGui.QLineEdit(self.tab_2)
        self.proxyUser.setObjectName("proxyUser")
        self.gridLayout_3.addWidget(self.proxyUser, 2, 1, 1, 1)
        self.label_20 = QtGui.QLabel(self.tab_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 3, 0, 1, 1)
        self.proxyPass = QtGui.QLineEdit(self.tab_2)
        self.proxyPass.setEchoMode(QtGui.QLineEdit.Password)
        self.proxyPass.setObjectName("proxyPass")
        self.gridLayout_3.addWidget(self.proxyPass, 3, 1, 1, 1)
        self.label_15 = QtGui.QLabel(self.tab_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 0, 2, 1, 1)
        self.proxyPort = QtGui.QSpinBox(self.tab_2)
        self.proxyPort.setMinimumSize(QtCore.QSize(60, 0))
        self.proxyPort.setObjectName("proxyPort")
        self.gridLayout_3.addWidget(self.proxyPort, 0, 3, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.label_12 = QtGui.QLabel(self.tab_2)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.saveAfterEvery = QtGui.QCheckBox(self.tab)
        self.saveAfterEvery.setChecked(True)
        self.saveAfterEvery.setObjectName("saveAfterEvery")
        self.gridLayout.addWidget(self.saveAfterEvery, 0, 0, 1, 1)
        self.saveAfterEveryNum = QtGui.QSpinBox(self.tab)
        self.saveAfterEveryNum.setMaximumSize(QtCore.QSize(60, 16777215))
        self.saveAfterEveryNum.setObjectName("saveAfterEveryNum")
        self.gridLayout.addWidget(self.saveAfterEveryNum, 0, 1, 1, 1)
        self.saveAfterAdding = QtGui.QCheckBox(self.tab)
        self.saveAfterAdding.setChecked(True)
        self.saveAfterAdding.setObjectName("saveAfterAdding")
        self.gridLayout.addWidget(self.saveAfterAdding, 1, 0, 1, 1)
        self.saveAfterAddingNum = QtGui.QSpinBox(self.tab)
        self.saveAfterAddingNum.setMaximumSize(QtCore.QSize(60, 16777215))
        self.saveAfterAddingNum.setObjectName("saveAfterAddingNum")
        self.gridLayout.addWidget(self.saveAfterAddingNum, 1, 1, 1, 1)
        self.saveWhenClosing = QtGui.QCheckBox(self.tab)
        self.saveWhenClosing.setChecked(True)
        self.saveWhenClosing.setObjectName("saveWhenClosing")
        self.gridLayout.addWidget(self.saveWhenClosing, 2, 0, 1, 2)
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.numBackups = QtGui.QSpinBox(self.tab)
        self.numBackups.setMinimumSize(QtCore.QSize(60, 0))
        self.numBackups.setMaximumSize(QtCore.QSize(60, 16777215))
        self.numBackups.setObjectName("numBackups")
        self.gridLayout_2.addWidget(self.numBackups, 0, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 3, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.openBackupFolder = QtGui.QLabel(self.tab)
        self.openBackupFolder.setObjectName("openBackupFolder")
        self.verticalLayout_3.addWidget(self.openBackupFolder)
        spacerItem3 = QtGui.QSpacerItem(20, 59, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.label_21 = QtGui.QLabel(self.tab)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_3.addWidget(self.label_21)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.vboxlayout1 = QtGui.QVBoxLayout(self.tab_3)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.gridlayout2 = QtGui.QGridLayout()
        self.gridlayout2.setObjectName("gridlayout2")
        self.label_6 = QtGui.QLabel(self.tab_3)
        self.label_6.setObjectName("label_6")
        self.gridlayout2.addWidget(self.label_6, 2, 0, 1, 1)
        self.showTimer = QtGui.QCheckBox(self.tab_3)
        self.showTimer.setObjectName("showTimer")
        self.gridlayout2.addWidget(self.showTimer, 6, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridlayout2.addItem(spacerItem4, 3, 0, 1, 1)
        self.alternativeTheme = QtGui.QCheckBox(self.tab_3)
        self.alternativeTheme.setObjectName("alternativeTheme")
        self.gridlayout2.addWidget(self.alternativeTheme, 4, 0, 1, 1)
        self.showStudyOptions = QtGui.QCheckBox(self.tab_3)
        self.showStudyOptions.setObjectName("showStudyOptions")
        self.gridlayout2.addWidget(self.showStudyOptions, 8, 0, 1, 1)
        self.showTray = QtGui.QCheckBox(self.tab_3)
        self.showTray.setObjectName("showTray")
        self.gridlayout2.addWidget(self.showTray, 7, 0, 1, 1)
        self.addZeroSpace = QtGui.QCheckBox(self.tab_3)
        self.addZeroSpace.setObjectName("addZeroSpace")
        self.gridlayout2.addWidget(self.addZeroSpace, 12, 0, 1, 1)
        self.openLastDeck = QtGui.QCheckBox(self.tab_3)
        self.openLastDeck.setObjectName("openLastDeck")
        self.gridlayout2.addWidget(self.openLastDeck, 9, 0, 1, 1)
        self.deckBrowserOrder = QtGui.QCheckBox(self.tab_3)
        self.deckBrowserOrder.setObjectName("deckBrowserOrder")
        self.gridlayout2.addWidget(self.deckBrowserOrder, 10, 0, 1, 1)
        self.deleteMedia = QtGui.QCheckBox(self.tab_3)
        self.deleteMedia.setObjectName("deleteMedia")
        self.gridlayout2.addWidget(self.deleteMedia, 11, 0, 1, 1)
        self.colourTimes = QtGui.QCheckBox(self.tab_3)
        self.colourTimes.setObjectName("colourTimes")
        self.gridlayout2.addWidget(self.colourTimes, 5, 0, 1, 1)
        self.vboxlayout1.addLayout(self.gridlayout2)
        spacerItem5 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.vboxlayout1.addItem(spacerItem5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_22 = QtGui.QLabel(self.tab_3)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout.addWidget(self.label_22)
        self.deckBrowserLen = QtGui.QSpinBox(self.tab_3)
        self.deckBrowserLen.setObjectName("deckBrowserLen")
        self.horizontalLayout.addWidget(self.deckBrowserLen)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.vboxlayout1.addLayout(self.horizontalLayout)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem7)
        self.label_8 = QtGui.QLabel(self.tab_3)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.vboxlayout1.addWidget(self.label_8)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(Preferences)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Help)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Preferences)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Preferences.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Preferences.reject)
        QtCore.QMetaObject.connectSlotsByName(Preferences)
        Preferences.setTabOrder(self.tabWidget, self.interfaceLang)
        Preferences.setTabOrder(self.interfaceLang, self.label_2)
        Preferences.setTabOrder(self.label_2, self.showDivider)
        Preferences.setTabOrder(self.showDivider, self.splitQA)
        Preferences.setTabOrder(self.splitQA, self.showEstimates)
        Preferences.setTabOrder(self.showEstimates, self.showProgress)
        Preferences.setTabOrder(self.showProgress, self.preventEdits)
        Preferences.setTabOrder(self.preventEdits, self.syncUser)
        Preferences.setTabOrder(self.syncUser, self.syncPass)
        Preferences.setTabOrder(self.syncPass, self.syncOnOpen)
        Preferences.setTabOrder(self.syncOnOpen, self.syncOnClose)
        Preferences.setTabOrder(self.syncOnClose, self.syncOnProgramOpen)
        Preferences.setTabOrder(self.syncOnProgramOpen, self.syncOnProgramClose)
        Preferences.setTabOrder(self.syncOnProgramClose, self.proxyHost)
        Preferences.setTabOrder(self.proxyHost, self.proxyPort)
        Preferences.setTabOrder(self.proxyPort, self.proxyUser)
        Preferences.setTabOrder(self.proxyUser, self.proxyPass)
        Preferences.setTabOrder(self.proxyPass, self.saveAfterEvery)
        Preferences.setTabOrder(self.saveAfterEvery, self.saveAfterEveryNum)
        Preferences.setTabOrder(self.saveAfterEveryNum, self.saveAfterAdding)
        Preferences.setTabOrder(self.saveAfterAdding, self.saveAfterAddingNum)
        Preferences.setTabOrder(self.saveAfterAddingNum, self.saveWhenClosing)
        Preferences.setTabOrder(self.saveWhenClosing, self.numBackups)
        Preferences.setTabOrder(self.numBackups, self.alternativeTheme)
        Preferences.setTabOrder(self.alternativeTheme, self.colourTimes)
        Preferences.setTabOrder(self.colourTimes, self.showTimer)
        Preferences.setTabOrder(self.showTimer, self.showTray)
        Preferences.setTabOrder(self.showTray, self.showStudyOptions)
        Preferences.setTabOrder(self.showStudyOptions, self.openLastDeck)
        Preferences.setTabOrder(self.openLastDeck, self.deckBrowserOrder)
        Preferences.setTabOrder(self.deckBrowserOrder, self.deleteMedia)
        Preferences.setTabOrder(self.deleteMedia, self.addZeroSpace)
        Preferences.setTabOrder(self.addZeroSpace, self.deckBrowserLen)
        Preferences.setTabOrder(self.deckBrowserLen, self.buttonBox)

    def retranslateUi(self, Preferences):
        Preferences.setWindowTitle(_("Preferences"))
        self.label.setText(_("<h1>Language</h1>"))
        self.label_2.setText(_("<h1>Reviewing</h1>"))
        self.showDivider.setText(_("Show divider between question and answer"))
        self.splitQA.setText(_("Put space between question and answer"))
        self.showEstimates.setText(_("Show next time before answer"))
        self.showProgress.setText(_("Show due count and progress during review"))
        self.preventEdits.setText(_("Prevent edits until answer shown"))
        self.label_3.setText(_("Some settings will take effect after you restart Anki."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _("Display"))
        self.label_16.setText(_("<h1>Synchronisation</h1><a href=\"http://anki.ichi2.net/\">Create a free account</a>."))
        self.label_18.setText(_("Password"))
        self.label_17.setText(_("Username"))
        self.syncOnClose.setText(_("Sync on deck close"))
        self.syncOnOpen.setText(_("Sync on deck open"))
        self.syncOnProgramOpen.setText(_("Sync on program open"))
        self.syncOnProgramClose.setText(_("Sync on program close"))
        self.label_13.setText(_("<h1>Proxy</h1>"))
        self.label_14.setText(_("Host"))
        self.label_19.setText(_("Username"))
        self.label_20.setText(_("Password"))
        self.label_15.setText(_("Port"))
        self.label_12.setText(_("Some settings will take effect after you restart Anki."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _("Network"))
        self.label_4.setText(_("<h1>Autosaving</h1>"))
        self.saveAfterEvery.setText(_("Save after answering"))
        self.saveAfterAdding.setText(_("Save after adding"))
        self.saveWhenClosing.setText(_("Save when closing"))
        self.label_5.setText(_("cards"))
        self.label_7.setText(_("facts"))
        self.label_9.setText(_("<h1>Backups</h1>Decks are backed up when they are opened, and only if they have been modified since the last backup."))
        self.label_10.setText(_("Keep"))
        self.label_11.setText(_("backups of each deck"))
        self.openBackupFolder.setText(_("<a href=\"backups\">Open backup folder</a>"))
        self.label_21.setText(_("Some settings will take effect after you restart Anki."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _("Saving"))
        self.label_6.setText(_("<h1>Advanced settings</h1>"))
        self.showTimer.setText(_("Show timer"))
        self.alternativeTheme.setText(_("Alternative theme"))
        self.showStudyOptions.setText(_("Show study options on deck load"))
        self.showTray.setText(_("Show tray icon"))
        self.addZeroSpace.setText(_("Add hidden char to text (fixes Thai on OSX)"))
        self.openLastDeck.setText(_("Always open last deck on startup"))
        self.deckBrowserOrder.setText(_("Show decks with cards due first in browser"))
        self.deleteMedia.setText(_("Delete original media on add"))
        self.colourTimes.setText(_("Colour next times"))
        self.label_22.setText(_("Max deck name length in deck browser:"))
        self.label_8.setText(_("Some settings will take effect after you restart Anki."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _("Advanced"))

