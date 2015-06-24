# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'B.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui,QtCore
import sys

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

class Ui_pag_B(QtGui.QWidget):
    def __init__(self):
        super(Ui_pag_B,self).__init__()
        self.nome = QtGui.QLabel('Nome')
        self.email = QtGui.QLabel('Email')
        self.senha = QtGui.QLabel('Senha')
        self.cadastrar = QtGui.QPushButton('Cadastrar')
        self.cancelarSO = QtGui.QPushButton('Cancelar')
        self.nome_2 = QtGui.QLineEdit()
        self.email_2 = QtGui.QLineEdit()
        self.senha_2 = QtGui.QLineEdit()
        layout = QGridLayout(self)
        layout.addWidget(self.nome, 0,0,1,1)
        layout.addWidget(self.email, 1,0,1,1)
        layout.addWidget(self.senha, 2,0,1,1)
        layout.addWidget(self.cadastrar, 3,1,1,1)
        layout.addWidget(self.cancelarSO, 3,0,1,1)
        layout.addWidget(self.nome_2, 0,1,1,1)
        layout.addWidget(self.email_2, 1,1,1,1)
        layout.addWidget(self.senha_2, 2,1,1,1)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = Ui_pag_B()
    win.show()
    app.exec_()