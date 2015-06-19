# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_LOGIN(object):
    def setupUi(self, LOGIN):
        LOGIN.setObjectName(_fromUtf8("LOGIN"))
        LOGIN.resize(600, 450)
        self.centralwidget = QtGui.QWidget(LOGIN)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.EMAIL_2 = QtGui.QLabel(self.centralwidget)
        self.EMAIL_2.setGeometry(QtCore.QRect(50, 130, 47, 13))
        self.EMAIL_2.setObjectName(_fromUtf8("EMAIL_2"))
        self.SENHA_2 = QtGui.QLabel(self.centralwidget)
        self.SENHA_2.setGeometry(QtCore.QRect(50, 190, 47, 13))
        self.SENHA_2.setObjectName(_fromUtf8("SENHA_2"))
        self.ENTRAR = QtGui.QPushButton(self.centralwidget)
        self.ENTRAR.setGeometry(QtCore.QRect(350, 370, 75, 31))
        self.ENTRAR.setDefault(False)
        self.ENTRAR.setObjectName(_fromUtf8("ENTRAR"))
        self.CADASTRAR = QtGui.QPushButton(self.centralwidget)
        self.CADASTRAR.setGeometry(QtCore.QRect(450, 370, 91, 31))
        self.CADASTRAR.setObjectName(_fromUtf8("CADASTRAR"))
        self.EMAIL_LOGIN = QtGui.QTextEdit(self.centralwidget)
        self.EMAIL_LOGIN.setGeometry(QtCore.QRect(130, 110, 431, 41))
        self.EMAIL_LOGIN.setObjectName(_fromUtf8("EMAIL_LOGIN"))
        self.SENHA_LOGIN = QtGui.QTextEdit(self.centralwidget)
        self.SENHA_LOGIN.setGeometry(QtCore.QRect(130, 180, 431, 41))
        self.SENHA_LOGIN.setObjectName(_fromUtf8("SENHA_LOGIN"))
        LOGIN.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(LOGIN)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        LOGIN.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(LOGIN)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        LOGIN.setStatusBar(self.statusbar)

        self.retranslateUi(LOGIN)
        QtCore.QMetaObject.connectSlotsByName(LOGIN)

    def retranslateUi(self, LOGIN):
        LOGIN.setWindowTitle(_translate("LOGIN", "MainWindow", None))
        self.EMAIL_2.setText(_translate("LOGIN", "E- MAIL", None))
        self.SENHA_2.setText(_translate("LOGIN", "SENHA", None))
        self.ENTRAR.setText(_translate("LOGIN", "ENTRAR", None))
        self.CADASTRAR.setText(_translate("LOGIN", "CADASTRAR-SE", None))

