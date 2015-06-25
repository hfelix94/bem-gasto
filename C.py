# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
from PyQt4 import QtCore, QtGui
from D import*
import sys
from firebase import firebase

login = {}
login["nome"] = "Phone 6 Gigante"
login["senha"] = "CM1287BRZ"

user1 = {'Nome': 'nome1', 'Senha': 'senha1'}
user2 = {'Nome': 'nome2', 'Senha': 'senha2'}

#login = [user1, user2]

# Uma lista de produtos
usuarios= []
usuarios.append(login)


# Troque esta URL pela de seu próprio App Firebase
FIREBASE_URL = "https://bem-gasto-controle.firebaseio.com/"

# Main
if __name__ == '__main__':

    fb = firebase.FirebaseApplication(FIREBASE_URL, None)

    # Escreve dados no Firebase
    fb.put('/', "Usuarios", usuarios)



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

class Ui_pag_C(QtGui.QWidget):
    def __init__(self):
        super(Ui_pag_C,self).__init__()
        self.email = QtGui.QLabel('Email')
        self.senha = QtGui.QLabel('Senha')
        self.entrar = QtGui.QPushButton('Entrar')
        self.cancelarSO = QtGui.QPushButton('Cancelar')
        self.email_2 = QtGui.QLineEdit()
        self.senha_2 = QtGui.QLineEdit()
        layout = QGridLayout(self)
        layout.addWidget(self.email, 0,0,1,1)
        layout.addWidget(self.senha, 1,0,1,1)
        layout.addWidget(self.entrar, 3,1,1,1)
        layout.addWidget(self.cancelarSO, 3,0,1,1)
        layout.addWidget(self.email_2, 0,1,1,1)
        layout.addWidget(self.senha_2, 1,1,1,1)
        self.pag_D = Ui_pag_D()
        layout_main = QGridLayout(self)
        layout_main.addWidget(self.pag_C, 0,0,1,1)
        layout_main.addWidget(self.pag_D, 0,0,1,1)
        self.pag_D.hide()


    def teste(self):
        self.pag_C.hide()
        self.pag_D.show()



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = Ui_pag_C()
    win.show()
    app.exec_()