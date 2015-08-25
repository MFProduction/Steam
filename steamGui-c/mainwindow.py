# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Oct 23 19:11:12 2014
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
        MainWindow.resize(707, 437)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.leTemp = QtGui.QLineEdit(self.centralWidget)
        self.leTemp.setObjectName(_fromUtf8("leTemp"))
        self.gridLayout.addWidget(self.leTemp, 1, 0, 1, 1)
        self.lePre = QtGui.QLineEdit(self.centralWidget)
        self.lePre.setObjectName(_fromUtf8("lePre"))
        self.gridLayout.addWidget(self.lePre, 1, 2, 1, 1)
        self.btnSubmit = QtGui.QPushButton(self.centralWidget)
        self.btnSubmit.setObjectName(_fromUtf8("btnSubmit"))
        self.gridLayout.addWidget(self.btnSubmit, 1, 3, 1, 1)
        self.listView = QtGui.QListView(self.centralWidget)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout.addWidget(self.listView, 2, 0, 1, 5)
        self.rbTP = QtGui.QRadioButton(self.centralWidget)
        self.rbTP.setObjectName(_fromUtf8("rbTP"))
        self.gridLayout.addWidget(self.rbTP, 0, 0, 1, 1)
        self.leRes = QtGui.QLineEdit(self.centralWidget)
        self.leRes.setObjectName(_fromUtf8("leRes"))
        self.gridLayout.addWidget(self.leRes, 1, 4, 1, 1)
        self.rbPh = QtGui.QRadioButton(self.centralWidget)
        self.rbPh.setObjectName(_fromUtf8("rbPh"))
        self.gridLayout.addWidget(self.rbPh, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 707, 29))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.leTemp.setText(QtGui.QApplication.translate("MainWindow", "400", None, QtGui.QApplication.UnicodeUTF8))
        self.lePre.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSubmit.setText(QtGui.QApplication.translate("MainWindow", "DO IT :)", None, QtGui.QApplication.UnicodeUTF8))
        self.rbTP.setText(QtGui.QApplication.translate("MainWindow", "T, P", None, QtGui.QApplication.UnicodeUTF8))
        self.rbPh.setText(QtGui.QApplication.translate("MainWindow", "P, h", None, QtGui.QApplication.UnicodeUTF8))

