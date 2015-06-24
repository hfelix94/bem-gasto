# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C.ui'
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

class Ui_pag_C(object):
    def setupUi(self, pag_C):
        pag_C.setObjectName(_fromUtf8("pag_C"))
        pag_C.resize(400, 300)
        self.nome = QtGui.QLabel(pag_C)
        self.nome.setGeometry(QtCore.QRect(30, 110, 47, 13))
        self.nome.setObjectName(_fromUtf8("nome"))
        self.senha = QtGui.QLabel(pag_C)
        self.senha.setGeometry(QtCore.QRect(30, 160, 47, 13))
        self.senha.setObjectName(_fromUtf8("senha"))
        self.nome_2 = QtGui.QLineEdit(pag_C)
        self.nome_2.setGeometry(QtCore.QRect(90, 110, 251, 20))
        self.nome_2.setText(_fromUtf8(""))
        self.nome_2.setObjectName(_fromUtf8("nome_2"))
        self.senha_2 = QtGui.QLineEdit(pag_C)
        self.senha_2.setGeometry(QtCore.QRect(90, 160, 251, 20))
        self.senha_2.setObjectName(_fromUtf8("senha_2"))
        self.entrar = QtGui.QPushButton(pag_C)
        self.entrar.setGeometry(QtCore.QRect(110, 240, 81, 31))
        self.entrar.setObjectName(_fromUtf8("entrar"))
        self.cancelar = QtGui.QPushButton(pag_C)
        self.cancelar.setGeometry(QtCore.QRect(230, 240, 81, 31))
        self.cancelar.setObjectName(_fromUtf8("cancelar"))

        self.retranslateUi(pag_C)
        QtCore.QMetaObject.connectSlotsByName(pag_C)

    def retranslateUi(self, pag_C):
        pag_C.setWindowTitle(_translate("pag_C", "Dialog", None))
        self.nome.setText(_translate("pag_C", "NOME", None))
        self.senha.setText(_translate("pag_C", "SENHA", None))
        self.entrar.setText(_translate("pag_C", "ENTRAR", None))
        self.cancelar.setText(_translate("pag_C", "CANCELAR", None))

