# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mw_menus.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from qtpy import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 717)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_2)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_5.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.groupBox_3)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.listWidget_2 = QtWidgets.QListWidget(self.frame)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.listWidget_2)
        self.gridLayout_5.addWidget(self.frame, 2, 0, 1, 2)
        self.listWidget = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.gridLayout_5.addWidget(self.listWidget, 1, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tabWidget.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tabWidget.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_12)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget.addTab(self.tab_12, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setLineWidth(0)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox, 1, 0, 1, 1)
        self.label_71 = QtWidgets.QLabel(self.centralwidget)
        self.label_71.setAlignment(QtCore.Qt.AlignCenter)
        self.label_71.setObjectName("label_71")
        self.gridLayout_7.addWidget(self.label_71, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 23))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuMenuSub = QtWidgets.QMenu(self.menuMenu)
        self.menuMenuSub.setObjectName("menuMenuSub")
        self.menuMenuDelayed = QtWidgets.QMenu(self.menubar)
        self.menuMenuDelayed.setObjectName("menuMenuDelayed")
        self.menuMenuSubDelayed = QtWidgets.QMenu(self.menuMenuDelayed)
        self.menuMenuSubDelayed.setObjectName("menuMenuSubDelayed")
        self.menuMenuCheckale = QtWidgets.QMenu(self.menubar)
        self.menuMenuCheckale.setObjectName("menuMenuCheckale")
        self.menuNew = QtWidgets.QMenu(self.menuMenuCheckale)
        self.menuNew.setObjectName("menuNew")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuMenuActionDis = QtWidgets.QMenu(self.menubar)
        self.menuMenuActionDis.setEnabled(True)
        self.menuMenuActionDis.setObjectName("menuMenuActionDis")
        self.menuMenuDisabled = QtWidgets.QMenu(self.menubar)
        self.menuMenuDisabled.setEnabled(False)
        self.menuMenuDisabled.setObjectName("menuMenuDisabled")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setIconSize(QtCore.QSize(16, 16))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBarDelayed = QtWidgets.QToolBar(MainWindow)
        self.toolBarDelayed.setObjectName("toolBarDelayed")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarDelayed)
        self.toolBarCheckable = QtWidgets.QToolBar(MainWindow)
        self.toolBarCheckable.setObjectName("toolBarCheckable")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarCheckable)
        MainWindow.insertToolBarBreak(self.toolBarCheckable)
        self.toolBarActionDis = QtWidgets.QToolBar(MainWindow)
        self.toolBarActionDis.setObjectName("toolBarActionDis")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarActionDis)
        self.actionActionA = QtWidgets.QAction(MainWindow)
        self.actionActionA.setObjectName("actionActionA")
        self.actionActionSubA = QtWidgets.QAction(MainWindow)
        self.actionActionSubA.setObjectName("actionActionSubA")
        self.actionActionSubB = QtWidgets.QAction(MainWindow)
        self.actionActionSubB.setObjectName("actionActionSubB")
        self.actionActionDelayedA = QtWidgets.QAction(MainWindow)
        self.actionActionDelayedA.setObjectName("actionActionDelayedA")
        self.actionActionDelayedSubA = QtWidgets.QAction(MainWindow)
        self.actionActionDelayedSubA.setObjectName("actionActionDelayedSubA")
        self.actionActionCheckableA = QtWidgets.QAction(MainWindow)
        self.actionActionCheckableA.setCheckable(True)
        self.actionActionCheckableA.setObjectName("actionActionCheckableA")
        self.actionActionCheckableSubAChecked = QtWidgets.QAction(MainWindow)
        self.actionActionCheckableSubAChecked.setCheckable(True)
        self.actionActionCheckableSubAChecked.setChecked(True)
        self.actionActionCheckableSubAChecked.setObjectName("actionActionCheckableSubAChecked")
        self.actionActionCheckableSubAUnchecked = QtWidgets.QAction(MainWindow)
        self.actionActionCheckableSubAUnchecked.setCheckable(True)
        self.actionActionCheckableSubAUnchecked.setObjectName("actionActionCheckableSubAUnchecked")
        self.actionNewB = QtWidgets.QAction(MainWindow)
        self.actionNewB.setObjectName("actionNewB")
        self.actionNewC = QtWidgets.QAction(MainWindow)
        self.actionNewC.setObjectName("actionNewC")
        self.actionNewD = QtWidgets.QAction(MainWindow)
        self.actionNewD.setObjectName("actionNewD")
        self.actionNewE = QtWidgets.QAction(MainWindow)
        self.actionNewE.setObjectName("actionNewE")
        self.actionActionIconADis = QtWidgets.QAction(MainWindow)
        self.actionActionIconADis.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/qss_icons/rc/window_undock_focus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionActionIconADis.setIcon(icon)
        self.actionActionIconADis.setObjectName("actionActionIconADis")
        self.actionActionIconB = QtWidgets.QAction(MainWindow)
        self.actionActionIconB.setEnabled(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/qss_icons/rc/window_close_focus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionActionIconB.setIcon(icon1)
        self.actionActionIconB.setObjectName("actionActionIconB")
        self.actionActionIconC = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/qss_icons/rc/arrow_right_focus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionActionIconC.setIcon(icon2)
        self.actionActionIconC.setObjectName("actionActionIconC")
        self.actionActionDis = QtWidgets.QAction(MainWindow)
        self.actionActionDis.setEnabled(False)
        self.actionActionDis.setObjectName("actionActionDis")
        self.actionActionCheckableCheckedDis = QtWidgets.QAction(MainWindow)
        self.actionActionCheckableCheckedDis.setCheckable(True)
        self.actionActionCheckableCheckedDis.setChecked(True)
        self.actionActionCheckableCheckedDis.setEnabled(False)
        self.actionActionCheckableCheckedDis.setObjectName("actionActionCheckableCheckedDis")
        self.actionActionCheckableUncheckedDis = QtWidgets.QAction(MainWindow)
        self.actionActionCheckableUncheckedDis.setCheckable(True)
        self.actionActionCheckableUncheckedDis.setEnabled(False)
        self.actionActionCheckableUncheckedDis.setObjectName("actionActionCheckableUncheckedDis")
        self.menuMenuSub.addAction(self.actionActionSubA)
        self.menuMenuSub.addAction(self.actionActionSubB)
        self.menuMenu.addAction(self.actionActionA)
        self.menuMenu.addAction(self.menuMenuSub.menuAction())
        self.menuMenu.addAction(self.actionActionIconADis)
        self.menuMenu.addAction(self.actionActionIconB)
        self.menuMenu.addAction(self.actionActionIconC)
        self.menuMenuSubDelayed.addAction(self.actionActionDelayedSubA)
        self.menuMenuDelayed.addAction(self.actionActionDelayedA)
        self.menuMenuDelayed.addAction(self.actionActionCheckableA)
        self.menuMenuDelayed.addAction(self.menuMenuSubDelayed.menuAction())
        self.menuNew.addSeparator()
        self.menuNew.addAction(self.actionNewB)
        self.menuNew.addAction(self.actionNewD)
        self.menuNew.addAction(self.actionNewC)
        self.menuNew.addSeparator()
        self.menuNew.addAction(self.actionNewE)
        self.menuMenuCheckale.addAction(self.actionActionCheckableA)
        self.menuMenuCheckale.addAction(self.actionActionIconADis)
        self.menuMenuCheckale.addAction(self.actionActionIconB)
        self.menuMenuCheckale.addAction(self.actionActionIconC)
        self.menuMenuCheckale.addSeparator()
        self.menuMenuCheckale.addAction(self.menuNew.menuAction())
        self.menuMenuActionDis.addAction(self.actionActionDis)
        self.menuMenuActionDis.addAction(self.actionActionCheckableCheckedDis)
        self.menuMenuActionDis.addAction(self.actionActionCheckableUncheckedDis)
        self.menuMenuActionDis.addAction(self.actionActionIconADis)
        self.menuMenuActionDis.addAction(self.actionActionIconB)
        self.menuMenuActionDis.addAction(self.actionActionIconC)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuMenuDelayed.menuAction())
        self.menubar.addAction(self.menuMenuCheckale.menuAction())
        self.menubar.addAction(self.menuMenuActionDis.menuAction())
        self.menubar.addAction(self.menuMenuDisabled.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.actionActionA)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionActionSubA)
        self.toolBar.addAction(self.actionActionSubB)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionActionIconADis)
        self.toolBar.addAction(self.actionActionIconB)
        self.toolBar.addAction(self.actionActionIconC)
        self.toolBarDelayed.addAction(self.actionActionDelayedA)
        self.toolBarDelayed.addSeparator()
        self.toolBarDelayed.addAction(self.actionActionDelayedSubA)
        self.toolBarCheckable.addAction(self.actionActionCheckableA)
        self.toolBarCheckable.addSeparator()
        self.toolBarCheckable.addAction(self.actionActionCheckableSubAChecked)
        self.toolBarCheckable.addAction(self.actionActionCheckableSubAUnchecked)
        self.toolBarActionDis.addAction(self.actionActionDis)
        self.toolBarActionDis.addAction(self.actionActionCheckableCheckedDis)
        self.toolBarActionDis.addAction(self.actionActionCheckableUncheckedDis)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.lineEdit_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Issue #115 - Tabs scroller buttons"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Issue #123 - Missing borders"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.lineEdit.setText(_translate("MainWindow", "Inside tab, outside frame"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.lineEdit_2.setText(_translate("MainWindow", "Inside tab and frame"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "ListWidget"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "ListWidget"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), _translate("MainWindow", "Page"))
        self.groupBox.setTitle(_translate("MainWindow", "Issue #112 - Hyperlinks color"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><a href=\"https://github.com/ColinDuquesnoy/QDarkStyleSheet/issues/112\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">Hyperlink Example</span></a></p><p align=\"center\"><span style=\" font-size:10pt; color:#7d7d7d;\">CSS for the documents (RichText) is not the same as the application. We cannot change the internal content CSS, e.g., hyperlinks. We suggest you use the middle tons (0-255, use 125), so this works for both white and dark theme (this color). The original color is the blue link on top.</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_71.setText(_translate("MainWindow", "Inside Central Widget"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuMenuSub.setTitle(_translate("MainWindow", "Menu Sub"))
        self.menuMenuDelayed.setTitle(_translate("MainWindow", "Menu Delayed"))
        self.menuMenuSubDelayed.setTitle(_translate("MainWindow", "Menu Sub Delayed"))
        self.menuMenuCheckale.setTitle(_translate("MainWindow", "Menu Checkable"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))
        self.menuAbout.setTitle(_translate("MainWindow", "About QDarkStyle"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuMenuActionDis.setTitle(_translate("MainWindow", "Menu Action Disabled"))
        self.menuMenuDisabled.setTitle(_translate("MainWindow", "Menu Disabled"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "Tool bar actions"))
        self.toolBarDelayed.setWindowTitle(_translate("MainWindow", "Tool bar actions delayed"))
        self.toolBarCheckable.setWindowTitle(_translate("MainWindow", "Tool bar action checkable"))
        self.toolBarActionDis.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.actionActionA.setText(_translate("MainWindow", "Action A"))
        self.actionActionSubA.setText(_translate("MainWindow", "Action A Sub"))
        self.actionActionSubA.setToolTip(_translate("MainWindow", "Action A Sub"))
        self.actionActionSubB.setText(_translate("MainWindow", "Action B Sub"))
        self.actionActionDelayedA.setText(_translate("MainWindow", "Action Delayed A"))
        self.actionActionDelayedA.setToolTip(_translate("MainWindow", "Action Delayed A"))
        self.actionActionDelayedSubA.setText(_translate("MainWindow", "Action Delayed Sub A"))
        self.actionActionDelayedSubA.setToolTip(_translate("MainWindow", "Action Delayed Sub A"))
        self.actionActionCheckableA.setText(_translate("MainWindow", "Action Checkable A"))
        self.actionActionCheckableA.setToolTip(_translate("MainWindow", "Action Checkable A"))
        self.actionActionCheckableSubAChecked.setText(_translate("MainWindow", "Action Checkable Sub A Checked"))
        self.actionActionCheckableSubAChecked.setToolTip(_translate("MainWindow", "Action Checkable Sub A Checked"))
        self.actionActionCheckableSubAUnchecked.setText(_translate("MainWindow", "Action Checkable Sub A Unchecked"))
        self.actionActionCheckableSubAUnchecked.setToolTip(_translate("MainWindow", "Action Checkable Sub A Unchecked"))
        self.actionNewB.setText(_translate("MainWindow", "New B"))
        self.actionNewC.setText(_translate("MainWindow", "New C"))
        self.actionNewD.setText(_translate("MainWindow", "New D"))
        self.actionNewE.setText(_translate("MainWindow", "New E"))
        self.actionActionIconADis.setText(_translate("MainWindow", "Action Icon A"))
        self.actionActionIconB.setText(_translate("MainWindow", "Action IconB"))
        self.actionActionIconB.setToolTip(_translate("MainWindow", "Action Icon B"))
        self.actionActionIconC.setText(_translate("MainWindow", "Action Icon C"))
        self.actionActionDis.setText(_translate("MainWindow", "Action Disabled"))
        self.actionActionDis.setToolTip(_translate("MainWindow", "Action Disabled"))
        self.actionActionCheckableCheckedDis.setText(_translate("MainWindow", "Action Checkable Checked Disabled"))
        self.actionActionCheckableCheckedDis.setToolTip(_translate("MainWindow", "Action Checkable Checked Disabled"))
        self.actionActionCheckableUncheckedDis.setText(_translate("MainWindow", "Action Checkable Unchecked Disabled"))
        self.actionActionCheckableUncheckedDis.setToolTip(_translate("MainWindow", "Action Checkable Unchecked Disabled"))
from qdarkstyle import style_rc
