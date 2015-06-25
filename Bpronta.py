# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'B.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from C import *




import sys
from PyQt4.QtGui import *
# para aproveitar a tela
class  Ui_pag_B(QWidget):

    def __init__(self):
        super( Ui_pag_B, self).__init__()
        self.entrar = QPushButton('Entrar')
        self.entrar.setGeometry(QtCore.QRect(140, 170, 111, 41))
        self.entrar.setObjectName("entrar")
        self.cadastrar = QPushButton('Cadastrar')
        self.cadastrar.setObjectName("cadastrar")
        self.cadastrar.clicked.connect(self.teste)
        self.pag_B = QWidget()
        layout.addWidget(self.email, 1,0,1,1)
        layout.addWidget(self.senha, 2,0,1,1)
        layout.addWidget(self.cadastrar, 3,1,1,1)
        layout.addWidget(self.cancelarSO, 3,0,1,1)
        layout.addWidget(self.email_2, 1,1,1,1)
        layout.addWidget(self.senha_2, 2,1,1,1)

    def teste(self):
        self.pag_B.hide()
        self.pag_C.show()











# acabou


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_pag_B()
    ex.show()
    sys.exit(app.exec_())