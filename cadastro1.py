# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro1.ui'
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

class Ui_CADASTRO1(object):
    def setupUi(self, CADASTRO1):
        CADASTRO1.setObjectName(_fromUtf8("CADASTRO1"))
        CADASTRO1.resize(550, 460)
        self.NOME_ = QtGui.QTextEdit(CADASTRO1)
        self.NOME_.setGeometry(QtCore.QRect(180, 20, 341, 31))
        self.NOME_.setObjectName(_fromUtf8("NOME_"))
        self.SOBRE_NOME = QtGui.QTextEdit(CADASTRO1)
        self.SOBRE_NOME.setGeometry(QtCore.QRect(180, 60, 341, 31))
        self.SOBRE_NOME.setObjectName(_fromUtf8("SOBRE_NOME"))
        self.CIDADE_ = QtGui.QTextEdit(CADASTRO1)
        self.CIDADE_.setGeometry(QtCore.QRect(180, 100, 341, 31))
        self.CIDADE_.setObjectName(_fromUtf8("CIDADE_"))
        self.ESTADO_ = QtGui.QTextEdit(CADASTRO1)
        self.ESTADO_.setGeometry(QtCore.QRect(180, 140, 341, 31))
        self.ESTADO_.setObjectName(_fromUtf8("ESTADO_"))
        self.EMAIL_ = QtGui.QTextEdit(CADASTRO1)
        self.EMAIL_.setGeometry(QtCore.QRect(180, 180, 341, 31))
        self.EMAIL_.setObjectName(_fromUtf8("EMAIL_"))
        self.SENHA_ = QtGui.QTextEdit(CADASTRO1)
        self.SENHA_.setGeometry(QtCore.QRect(180, 260, 341, 31))
        self.SENHA_.setObjectName(_fromUtf8("SENHA_"))
        self.CONFIRMA_SENHA = QtGui.QTextEdit(CADASTRO1)
        self.CONFIRMA_SENHA.setGeometry(QtCore.QRect(180, 300, 341, 31))
        self.CONFIRMA_SENHA.setObjectName(_fromUtf8("CONFIRMA_SENHA"))
        self.CONFIRMA_EMAIL = QtGui.QTextEdit(CADASTRO1)
        self.CONFIRMA_EMAIL.setGeometry(QtCore.QRect(180, 220, 341, 31))
        self.CONFIRMA_EMAIL.setObjectName(_fromUtf8("CONFIRMA_EMAIL"))
        self.NOME = QtGui.QLabel(CADASTRO1)
        self.NOME.setGeometry(QtCore.QRect(30, 30, 47, 13))
        self.NOME.setObjectName(_fromUtf8("NOME"))
        self.SOBRENOME = QtGui.QLabel(CADASTRO1)
        self.SOBRENOME.setGeometry(QtCore.QRect(30, 70, 71, 16))
        self.SOBRENOME.setObjectName(_fromUtf8("SOBRENOME"))
        self.CIDADE = QtGui.QLabel(CADASTRO1)
        self.CIDADE.setGeometry(QtCore.QRect(30, 110, 47, 13))
        self.CIDADE.setObjectName(_fromUtf8("CIDADE"))
        self.ESTADO = QtGui.QLabel(CADASTRO1)
        self.ESTADO.setGeometry(QtCore.QRect(30, 150, 47, 13))
        self.ESTADO.setObjectName(_fromUtf8("ESTADO"))
        self.EMAIL = QtGui.QLabel(CADASTRO1)
        self.EMAIL.setGeometry(QtCore.QRect(30, 190, 47, 13))
        self.EMAIL.setObjectName(_fromUtf8("EMAIL"))
        self.CONFIRMAEMAIL = QtGui.QLabel(CADASTRO1)
        self.CONFIRMAEMAIL.setGeometry(QtCore.QRect(30, 230, 151, 16))
        self.CONFIRMAEMAIL.setObjectName(_fromUtf8("CONFIRMAEMAIL"))
        self.label_7 = QtGui.QLabel(CADASTRO1)
        self.label_7.setGeometry(QtCore.QRect(30, 270, 47, 13))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.CONFIRMASENHA = QtGui.QLabel(CADASTRO1)
        self.CONFIRMASENHA.setGeometry(QtCore.QRect(30, 310, 141, 16))
        self.CONFIRMASENHA.setObjectName(_fromUtf8("CONFIRMASENHA"))
        self.SEGUINTE = QtGui.QPushButton(CADASTRO1)
        self.SEGUINTE.setGeometry(QtCore.QRect(340, 410, 75, 31))
        self.SEGUINTE.setObjectName(_fromUtf8("SEGUINTE"))
        self.CANCELAR = QtGui.QPushButton(CADASTRO1)
        self.CANCELAR.setGeometry(QtCore.QRect(430, 410, 75, 31))
        self.CANCELAR.setObjectName(_fromUtf8("CANCELAR"))

        self.retranslateUi(CADASTRO1)
        QtCore.QMetaObject.connectSlotsByName(CADASTRO1)

    def retranslateUi(self, CADASTRO1):
        CADASTRO1.setWindowTitle(_translate("CADASTRO1", "Dialog", None))
        self.NOME.setText(_translate("CADASTRO1", "NOME", None))
        self.SOBRENOME.setText(_translate("CADASTRO1", "SOBRENOME", None))
        self.CIDADE.setText(_translate("CADASTRO1", "CIDADE", None))
        self.ESTADO.setText(_translate("CADASTRO1", "ESTADO", None))
        self.EMAIL.setText(_translate("CADASTRO1", "E-MAIL", None))
        self.CONFIRMAEMAIL.setText(_translate("CADASTRO1", "CONFIRMAÇÃO DO E-MAIL", None))
        self.label_7.setText(_translate("CADASTRO1", "SENHA", None))
        self.CONFIRMASENHA.setText(_translate("CADASTRO1", "CONFIRMAÇÃO DA SENHA", None))
        self.SEGUINTE.setText(_translate("CADASTRO1", "SEGUINTE", None))
        self.CANCELAR.setText(_translate("CADASTRO1", "CANCELAR", None))

