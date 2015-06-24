# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H.ui'
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

class Ui_pag_dica(object):
    def setupUi(self, pag_dica):
        pag_dica.setObjectName(_fromUtf8("pag_dica"))
        pag_dica.resize(400, 300)
        self.sair = QtGui.QPushButton(pag_dica)
        self.sair.setGeometry(QtCore.QRect(280, 250, 75, 23))
        self.sair.setObjectName(_fromUtf8("sair"))
        self.dica_dia = QtGui.QLineEdit(pag_dica)
        self.dica_dia.setGeometry(QtCore.QRect(40, 60, 311, 151))
        self.dica_dia.setObjectName(_fromUtf8("dica_dia"))
        self.dica_do_dia = QtGui.QLabel(pag_dica)
        self.dica_do_dia.setGeometry(QtCore.QRect(40, 30, 71, 16))
        self.dica_do_dia.setObjectName(_fromUtf8("dica_do_dia"))

        self.retranslateUi(pag_dica)
        QtCore.QMetaObject.connectSlotsByName(pag_dica)

    def retranslateUi(self, pag_dica):
        pag_dica.setWindowTitle(_translate("pag_dica", "Dialog", None))
        self.sair.setText(_translate("pag_dica", "SAIR", None))
        self.dica_do_dia.setText(_translate("pag_dica", "DICA DO DIA", None))

