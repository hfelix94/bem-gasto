# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E.ui'
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

class Ui_pag_E(object):
    def setupUi(self, pag_E):
        pag_E.setObjectName(_fromUtf8("pag_E"))
        pag_E.resize(254, 111)
        self.sim = QtGui.QPushButton(pag_E)
        self.sim.setGeometry(QtCore.QRect(30, 60, 81, 31))
        self.sim.setObjectName(_fromUtf8("sim"))
        self.nao = QtGui.QPushButton(pag_E)
        self.nao.setGeometry(QtCore.QRect(140, 60, 81, 31))
        self.nao.setObjectName(_fromUtf8("nao"))
        self.sair = QtGui.QLabel(pag_E)
        self.sair.setGeometry(QtCore.QRect(30, 20, 47, 13))
        self.sair.setObjectName(_fromUtf8("sair"))

        self.retranslateUi(pag_E)
        QtCore.QMetaObject.connectSlotsByName(pag_E)

    def retranslateUi(self, pag_E):
        pag_E.setWindowTitle(_translate("pag_E", "Dialog", None))
        self.sim.setText(_translate("pag_E", "SIM", None))
        self.nao.setText(_translate("pag_E", "NÃO", None))
        self.sair.setText(_translate("pag_E", "SAIR ?", None))

