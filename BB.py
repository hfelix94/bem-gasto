# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'B.ui'
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

class Ui_pag_B(object):
    def setupUi(self, pag_B):
        pag_B.setObjectName(_fromUtf8("pag_B"))
        pag_B.resize(400, 300)
        self.nome = QtGui.QLabel(pag_B)
        self.nome.setGeometry(QtCore.QRect(20, 90, 47, 13))
        self.nome.setObjectName(_fromUtf8("nome"))
        self.email = QtGui.QLabel(pag_B)
        self.email.setGeometry(QtCore.QRect(20, 140, 47, 13))
        self.email.setObjectName(_fromUtf8("email"))
        self.senha = QtGui.QLabel(pag_B)
        self.senha.setGeometry(QtCore.QRect(20, 190, 47, 13))
        self.senha.setObjectName(_fromUtf8("senha"))
        self.cadastrar = QtGui.QPushButton(pag_B)
        self.cadastrar.setGeometry(QtCore.QRect(80, 242, 81, 31))
        self.cadastrar.setObjectName(_fromUtf8("cadastrar"))
        self.cancelarSO = QtGui.QPushButton(pag_B)
        self.cancelarSO.setGeometry(QtCore.QRect(220, 242, 91, 31))
        self.cancelarSO.setObjectName(_fromUtf8("cancelarSO"))
        self.nome_2 = QtGui.QLineEdit(pag_B)
        self.nome_2.setGeometry(QtCore.QRect(80, 90, 261, 20))
        self.nome_2.setObjectName(_fromUtf8("nome_2"))
        self.email_2 = QtGui.QLineEdit(pag_B)
        self.email_2.setGeometry(QtCore.QRect(80, 140, 261, 20))
        self.email_2.setObjectName(_fromUtf8("email_2"))
        self.senha_2 = QtGui.QLineEdit(pag_B)
        self.senha_2.setGeometry(QtCore.QRect(80, 190, 261, 20))
        self.senha_2.setObjectName(_fromUtf8("senha_2"))

        self.retranslateUi(pag_B)
        QtCore.QMetaObject.connectSlotsByName(pag_B)

    def retranslateUi(self, pag_B):
        pag_B.setWindowTitle(_translate("pag_B", "Dialog", None))
        self.nome.setText(_translate("pag_B", "NOME", None))
        self.email.setText(_translate("pag_B", "E-MAIL", None))
        self.senha.setText(_translate("pag_B", "SENHA", None))
        self.cadastrar.setText(_translate("pag_B", "CADASTRAR", None))
        self.cancelarSO.setText(_translate("pag_B", "CANCELAR", None))

