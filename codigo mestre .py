

import sys
from PyQt4.QtGui import *
# para aproveitar a tela
class Aplicativo(QWidget):

    def __init__(self):
        super(Aplicativo, self).__init__()
        self.pushButton = QPushButton('teste')
        self.pushButton.clicked.connect(self.teste)
        self.pag_A = QWidget()
        layout_1 = QVBoxLayout(self.pag_A)
        layout_1.addWidget(QLabel('janela1'))
        layout_1.addWidget(self.pushButton)
        self.pag_B = QWidget()
        layout_2 = QVBoxLayout(self.pag_B)
        layout_2.addWidget(QLabel('janela2'))
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
    ex = Aplicativo()
    ex.show()
    sys.exit(app.exec_())