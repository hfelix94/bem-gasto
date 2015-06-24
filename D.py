# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D.ui'
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

class Ui_pag_D(object):
    def setupUi(self, pag_D):
        pag_D.setObjectName(_fromUtf8("pag_D"))
        pag_D.resize(400, 300)
        self.meus_ativos = QtGui.QPushButton(pag_D)
        self.meus_ativos.setGeometry(QtCore.QRect(50, 80, 251, 31))
        self.meus_ativos.setObjectName(_fromUtf8("meus_ativos"))
        self.meus_passivos = QtGui.QPushButton(pag_D)
        self.meus_passivos.setGeometry(QtCore.QRect(50, 130, 251, 31))
        self.meus_passivos.setObjectName(_fromUtf8("meus_passivos"))
        self.dica_do_dia = QtGui.QPushButton(pag_D)
        self.dica_do_dia.setGeometry(QtCore.QRect(50, 180, 251, 31))
        self.dica_do_dia.setObjectName(_fromUtf8("dica_do_dia"))
        self.sair = QtGui.QPushButton(pag_D)
        self.sair.setGeometry(QtCore.QRect(50, 260, 75, 23))
        self.sair.setObjectName(_fromUtf8("sair"))

        self.retranslateUi(pag_D)
        QtCore.QMetaObject.connectSlotsByName(pag_D)

    def retranslateUi(self, pag_D):
        pag_D.setWindowTitle(_translate("pag_D", "Dialog", None))
        self.meus_ativos.setText(_translate("pag_D", "MEUS ATIVOS", None))
        self.meus_passivos.setText(_translate("pag_D", "MEUS PASSIVOS", None))
        self.dica_do_dia.setText(_translate("pag_D", "DICA DO DIA", None))
        self.sair.setText(_translate("pag_D", "SAIR", None))

