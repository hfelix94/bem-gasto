from cadastro_gerado import *
from login_gerado import *

import sys
from PyQt4.QtGui import *
# para aproveitar a tela
class Aplicativo(QWidget):

    def __init__(self):
        super(Aplicativo, self).__init__()
        self.pushButton = QPushButton('teste')
        self.pushButton.clicked.connect(self.teste)
        self.janela1 = QWidget()
        layout_1 = QVBoxLayout(self.janela1)
        layout_1.addWidget(QLabel('janela1'))
        layout_1.addWidget(self.pushButton)
        self.janela2 = QWidget()
        layout_2 = QVBoxLayout(self.janela2)
        layout_2.addWidget(QLabel('janela2'))
        layout_main = QGridLayout(self)
        layout_main.addWidget(self.janela1, 0,0,1,1)
        layout_main.addWidget(self.janela2, 0,0,1,1)
        self.janela2.hide()

    def teste(self):
        self.janela1.hide()
        self.janela2.show()











# acabou


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = Aplicativo()
   ex.show()
   sys.exit(app.exec_()