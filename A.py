# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'A.ui'
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

class Ui_pag_A(object):
    def setupUi(self, pag_A):
        pag_A.setObjectName(_fromUtf8("pag_A"))
        pag_A.resize(400, 300)
        self.cadastrar = QtGui.QPushButton(pag_A)
        self.cadastrar.setGeometry(QtCore.QRect(140, 230, 111, 41))
        self.cadastrar.setObjectName(_fromUtf8("cadastrar"))
        self.entrar = QtGui.QPushButton(pag_A)
        self.entrar.setGeometry(QtCore.QRect(140, 170, 111, 41))
        self.entrar.setObjectName(_fromUtf8("entrar"))

        self.retranslateUi(pag_A)
        QtCore.QMetaObject.connectSlotsByName(pag_A)

    def retranslateUi(self, pag_A):
        pag_A.setWindowTitle(_translate("pag_A", "Dialog", None))
        self.cadastrar.setText(_translate("pag_A", "CADASTRAR", None))
        self.entrar.setText(_translate("pag_A", "ENTRAR", None))

