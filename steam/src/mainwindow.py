# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mrstain/Projekti/Steam/steamGui-c/mainwindow.ui'
#
# Created: Wed Nov  5 17:09:39 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(366, 432)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.rbTP = QtGui.QRadioButton(self.centralWidget)
        self.rbTP.setObjectName(_fromUtf8("rbTP"))
        self.horizontalLayout.addWidget(self.rbTP)
        self.rbPh = QtGui.QRadioButton(self.centralWidget)
        self.rbPh.setObjectName(_fromUtf8("rbPh"))
        self.horizontalLayout.addWidget(self.rbPh)
        self.rbPs = QtGui.QRadioButton(self.centralWidget)
        self.rbPs.setObjectName(_fromUtf8("rbPs"))
        self.horizontalLayout.addWidget(self.rbPs)
        self.rbhs = QtGui.QRadioButton(self.centralWidget)
        self.rbhs.setObjectName(_fromUtf8("rbhs"))
        self.horizontalLayout.addWidget(self.rbhs)
        self.rbTx = QtGui.QRadioButton(self.centralWidget)
        self.rbTx.setObjectName(_fromUtf8("rbTx"))
        self.horizontalLayout.addWidget(self.rbTx)
        self.rbPx = QtGui.QRadioButton(self.centralWidget)
        self.rbPx.setObjectName(_fromUtf8("rbPx"))
        self.horizontalLayout.addWidget(self.rbPx)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.la1 = QtGui.QLabel(self.centralWidget)
        self.la1.setObjectName(_fromUtf8("la1"))
        self.horizontalLayout_2.addWidget(self.la1)
        self.le1 = QtGui.QLineEdit(self.centralWidget)
        self.le1.setObjectName(_fromUtf8("le1"))
        self.horizontalLayout_2.addWidget(self.le1)
        self.la2 = QtGui.QLabel(self.centralWidget)
        self.la2.setObjectName(_fromUtf8("la2"))
        self.horizontalLayout_2.addWidget(self.la2)
        self.le2 = QtGui.QLineEdit(self.centralWidget)
        self.le2.setObjectName(_fromUtf8("le2"))
        self.horizontalLayout_2.addWidget(self.le2)
        self.btnShow = QtGui.QPushButton(self.centralWidget)
        self.btnShow.setObjectName(_fromUtf8("btnShow"))
        self.horizontalLayout_2.addWidget(self.btnShow)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidget = QtGui.QTableWidget(self.centralWidget)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.scrollArea = QtGui.QScrollArea(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 82, 308))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 366, 29))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.rbTP.setText(QtGui.QApplication.translate("MainWindow", "T, P", None, QtGui.QApplication.UnicodeUTF8))
        self.rbPh.setText(QtGui.QApplication.translate("MainWindow", "P, h", None, QtGui.QApplication.UnicodeUTF8))
        self.rbPs.setText(QtGui.QApplication.translate("MainWindow", "P, s", None, QtGui.QApplication.UnicodeUTF8))
        self.rbhs.setText(QtGui.QApplication.translate("MainWindow", "h, s", None, QtGui.QApplication.UnicodeUTF8))
        self.rbTx.setText(QtGui.QApplication.translate("MainWindow", "T, x", None, QtGui.QApplication.UnicodeUTF8))
        self.rbPx.setText(QtGui.QApplication.translate("MainWindow", "P, x", None, QtGui.QApplication.UnicodeUTF8))
        self.la1.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.la2.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.btnShow.setText(QtGui.QApplication.translate("MainWindow", "Show", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))

