# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ativos.ui'
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

class Ui_ATIVOSEPASSIVOS(object):
    def setupUi(self, ATIVOSEPASSIVOS):
        ATIVOSEPASSIVOS.setObjectName(_fromUtf8("ATIVOSEPASSIVOS"))
        ATIVOSEPASSIVOS.resize(400, 400)
        self.ATIVOS = QtGui.QTextEdit(ATIVOSEPASSIVOS)
        self.ATIVOS.setGeometry(QtCore.QRect(120, 40, 201, 31))
        self.ATIVOS.setObjectName(_fromUtf8("ATIVOS"))
        self.PASSIVOS_2 = QtGui.QTextEdit(ATIVOSEPASSIVOS)
        self.PASSIVOS_2.setGeometry(QtCore.QRect(120, 100, 201, 31))
        self.PASSIVOS_2.setObjectName(_fromUtf8("PASSIVOS_2"))
        self.ATIVOS_2 = QtGui.QLabel(ATIVOSEPASSIVOS)
        self.ATIVOS_2.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.ATIVOS_2.setObjectName(_fromUtf8("ATIVOS_2"))
        self.PASSIVOS = QtGui.QLabel(ATIVOSEPASSIVOS)
        self.PASSIVOS.setGeometry(QtCore.QRect(20, 110, 61, 21))
        self.PASSIVOS.setObjectName(_fromUtf8("PASSIVOS"))
        self.CATEGORIA_2 = QtGui.QComboBox(ATIVOSEPASSIVOS)
        self.CATEGORIA_2.setGeometry(QtCore.QRect(120, 170, 101, 22))
        self.CATEGORIA_2.setObjectName(_fromUtf8("CATEGORIA_2"))
        self.CATEGORIA_2.addItem(_fromUtf8(""))
        self.CATEGORIA_2.setItemText(0, _fromUtf8(""))
        self.CATEGORIA_2.addItem(_fromUtf8(""))
        self.CATEGORIA_2.addItem(_fromUtf8(""))
        self.CATEGORIA_2.addItem(_fromUtf8(""))
        self.CATEGORIA_2.addItem(_fromUtf8(""))
        self.CATEGORIA_2.addItem(_fromUtf8(""))
        self.CATEGORIA_2.addItem(_fromUtf8(""))
        self.CATEGORIA = QtGui.QLabel(ATIVOSEPASSIVOS)
        self.CATEGORIA.setGeometry(QtCore.QRect(20, 170, 81, 16))
        self.CATEGORIA.setObjectName(_fromUtf8("CATEGORIA"))
        self.OK = QtGui.QPushButton(ATIVOSEPASSIVOS)
        self.OK.setGeometry(QtCore.QRect(200, 342, 75, 31))
        self.OK.setObjectName(_fromUtf8("OK"))
        self.CANCELAR = QtGui.QPushButton(ATIVOSEPASSIVOS)
        self.CANCELAR.setGeometry(QtCore.QRect(300, 340, 75, 31))
        self.CANCELAR.setObjectName(_fromUtf8("CANCELAR"))

        self.retranslateUi(ATIVOSEPASSIVOS)
        QtCore.QMetaObject.connectSlotsByName(ATIVOSEPASSIVOS)

    def retranslateUi(self, ATIVOSEPASSIVOS):
        ATIVOSEPASSIVOS.setWindowTitle(_translate("ATIVOSEPASSIVOS", "Dialog", None))
        self.ATIVOS_2.setText(_translate("ATIVOSEPASSIVOS", "ATIVOS", None))
        self.PASSIVOS.setText(_translate("ATIVOSEPASSIVOS", "PASSIVOS", None))
        self.CATEGORIA_2.setItemText(1, _translate("ATIVOSEPASSIVOS", "Alimentação", None))
        self.CATEGORIA_2.setItemText(2, _translate("ATIVOSEPASSIVOS", "Transporte", None))
        self.CATEGORIA_2.setItemText(3, _translate("ATIVOSEPASSIVOS", "Moradia", None))
        self.CATEGORIA_2.setItemText(4, _translate("ATIVOSEPASSIVOS", "Saúde", None))
        self.CATEGORIA_2.setItemText(5, _translate("ATIVOSEPASSIVOS", "Lazer", None))
        self.CATEGORIA_2.setItemText(6, _translate("ATIVOSEPASSIVOS", "Outros", None))
        self.CATEGORIA.setText(_translate("ATIVOSEPASSIVOS", "CATEGORIA", None))
        self.OK.setText(_translate("ATIVOSEPASSIVOS", "OK", None))
        self.CANCELAR.setText(_translate("ATIVOSEPASSIVOS", "CANCELAR", None))

