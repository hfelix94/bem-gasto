# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'A.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from B import *

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

class Ui_pag(object):
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



import sys
from PyQt4.QtGui import *
# para aproveitar a tela
class  Ui_pag_A(QWidget):

    def __init__(self):
        super( Ui_pag_A, self).__init__()
        self.entrar = QPushButton('Entrar')
        self.entrar.setGeometry(QtCore.QRect(140, 170, 111, 41))
        self.entrar.setObjectName(_fromUtf8("entrar"))
        self.cadastrar = QPushButton('Cadastrar')
        self.cadastrar.setObjectName("cadastrar")
        self.cadastrar.clicked.connect(self.teste)
        self.pag_A = QWidget()
        layout_1 = QVBoxLayout(self.pag_A)
        layout_1.addWidget(QLabel('janela1'))
        layout_1.addWidget(self.cadastrar)
        layout_1.addWidget(self.entrar)
        self.pag_B = Ui_pag_B()
        layout_main = QGridLayout(self)
        layout_main.addWidget(self.pag_A, 0,0,1,1)
        layout_main.addWidget(self.pag_B, 0,0,1,1)
        self.pag_B.hide()


    def teste(self):
        self.pag_A.hide()
        self.pag_B.show()











# acabou


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_pag_A()
    ex.show()
    sys.exit(app.exec_())