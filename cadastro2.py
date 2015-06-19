# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro2.ui'
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

class Ui_CADASTRO22(object):
    def setupUi(self, CADASTRO22):
        CADASTRO22.setObjectName(_fromUtf8("CADASTRO22"))
        CADASTRO22.resize(535, 480)
        self.RENDAMENSAL = QtGui.QLabel(CADASTRO22)
        self.RENDAMENSAL.setGeometry(QtCore.QRect(10, 50, 141, 16))
        self.RENDAMENSAL.setObjectName(_fromUtf8("RENDAMENSAL"))
        self.TRANSPORTEMENSAL = QtGui.QLabel(CADASTRO22)
        self.TRANSPORTEMENSAL.setGeometry(QtCore.QRect(10, 110, 201, 16))
        self.TRANSPORTEMENSAL.setObjectName(_fromUtf8("TRANSPORTEMENSAL"))
        self.ALIMENTAOMENSAL = QtGui.QLabel(CADASTRO22)
        self.ALIMENTAOMENSAL.setGeometry(QtCore.QRect(10, 170, 191, 16))
        self.ALIMENTAOMENSAL.setObjectName(_fromUtf8("ALIMENTAOMENSAL"))
        self.MORADIAMENSAL = QtGui.QLabel(CADASTRO22)
        self.MORADIAMENSAL.setGeometry(QtCore.QRect(10, 230, 171, 16))
        self.MORADIAMENSAL.setObjectName(_fromUtf8("MORADIAMENSAL"))
        self.LAZERMENSAL = QtGui.QLabel(CADASTRO22)
        self.LAZERMENSAL.setGeometry(QtCore.QRect(10, 290, 151, 16))
        self.LAZERMENSAL.setObjectName(_fromUtf8("LAZERMENSAL"))
        self.CONTINUAR = QtGui.QPushButton(CADASTRO22)
        self.CONTINUAR.setGeometry(QtCore.QRect(330, 430, 75, 23))
        self.CONTINUAR.setObjectName(_fromUtf8("CONTINUAR"))
        self.CANCELAR_2 = QtGui.QPushButton(CADASTRO22)
        self.CANCELAR_2.setGeometry(QtCore.QRect(420, 430, 75, 23))
        self.CANCELAR_2.setObjectName(_fromUtf8("CANCELAR_2"))
        self.RENDA_MENSAL = QtGui.QTextEdit(CADASTRO22)
        self.RENDA_MENSAL.setGeometry(QtCore.QRect(200, 40, 311, 31))
        self.RENDA_MENSAL.setObjectName(_fromUtf8("RENDA_MENSAL"))
        self.TRANSPORTE_MENSAL = QtGui.QTextEdit(CADASTRO22)
        self.TRANSPORTE_MENSAL.setGeometry(QtCore.QRect(200, 100, 311, 31))
        self.TRANSPORTE_MENSAL.setObjectName(_fromUtf8("TRANSPORTE_MENSAL"))
        self.ALIMENTACAO_MENSAL = QtGui.QTextEdit(CADASTRO22)
        self.ALIMENTACAO_MENSAL.setGeometry(QtCore.QRect(200, 160, 311, 31))
        self.ALIMENTACAO_MENSAL.setObjectName(_fromUtf8("ALIMENTACAO_MENSAL"))
        self.MORADIA_MENSAL = QtGui.QTextEdit(CADASTRO22)
        self.MORADIA_MENSAL.setGeometry(QtCore.QRect(200, 220, 311, 31))
        self.MORADIA_MENSAL.setObjectName(_fromUtf8("MORADIA_MENSAL"))
        self.LAZER_MENSAL = QtGui.QTextEdit(CADASTRO22)
        self.LAZER_MENSAL.setGeometry(QtCore.QRect(200, 280, 311, 31))
        self.LAZER_MENSAL.setObjectName(_fromUtf8("LAZER_MENSAL"))
        self.OUTROS_GASTOS = QtGui.QTextEdit(CADASTRO22)
        self.OUTROS_GASTOS.setGeometry(QtCore.QRect(200, 340, 311, 31))
        self.OUTROS_GASTOS.setObjectName(_fromUtf8("OUTROS_GASTOS"))
        self.OUTROSGASTOS = QtGui.QLabel(CADASTRO22)
        self.OUTROSGASTOS.setGeometry(QtCore.QRect(10, 350, 111, 16))
        self.OUTROSGASTOS.setObjectName(_fromUtf8("OUTROSGASTOS"))

        self.retranslateUi(CADASTRO22)
        QtCore.QMetaObject.connectSlotsByName(CADASTRO22)

    def retranslateUi(self, CADASTRO22):
        CADASTRO22.setWindowTitle(_translate("CADASTRO22", "Dialog", None))
        self.RENDAMENSAL.setText(_translate("CADASTRO22", "QUAL A SUA RENDA MENSAL", None))
        self.TRANSPORTEMENSAL.setText(_translate("CADASTRO22", "QUAL SEU GASTO COM TRANSPORTE", None))
        self.ALIMENTAOMENSAL.setText(_translate("CADASTRO22", "QUAL SEU GASTO COM ALIMENTAÇÃO", None))
        self.MORADIAMENSAL.setText(_translate("CADASTRO22", "QUAL SEU GASTO COM MORADIA", None))
        self.LAZERMENSAL.setText(_translate("CADASTRO22", "QUAL SEU GASTO COM LAZER", None))
        self.CONTINUAR.setText(_translate("CADASTRO22", "CONTINUAR", None))
        self.CANCELAR_2.setText(_translate("CADASTRO22", "CANCELAR", None))
        self.OUTROSGASTOS.setText(_translate("CADASTRO22", "OUTROS GASTOS", None))

