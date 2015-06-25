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

class Ui_pag_D(QtGui.QWidget):
    def __init__(self):
        super(Ui_pag_D,self).__init__()
        self.ativos = QtGui.QPushButton('ATIVOS')
        self.passivos = QtGui.QPushButton('PASSIVOS')
        self.dicas = QtGui.QPushButton('DICA DO DIA')
        self.sair = QtGui.QPushButton('SAIR')
        layout = QGridLayout(self)
        layout.addWidget(self.ativos, 3,0,1,1)
        layout.addWidget(self.passivos, 3,1,1,1)
        layout.addWidget(self.dicas, 3,2,1,1)
        layout.addWidget(self.sair, 3,3,1,1)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = Ui_pag_D()
    win.show()
    app.exec_()