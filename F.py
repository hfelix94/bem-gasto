# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F.ui'
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

class Ui_pag_F(object):
    def setupUi(self, pag_F):
        pag_F.setObjectName(_fromUtf8("pag_F"))
        pag_F.resize(431, 431)
        self.ativos = QtGui.QLabel(pag_F)
        self.ativos.setGeometry(QtCore.QRect(30, 40, 47, 13))
        self.ativos.setObjectName(_fromUtf8("ativos"))
        self.adicionar_ativo = QtGui.QPushButton(pag_F)
        self.adicionar_ativo.setGeometry(QtCore.QRect(160, 130, 111, 23))
        self.adicionar_ativo.setObjectName(_fromUtf8("adicionar_ativo"))
        self.ativo = QtGui.QLineEdit(pag_F)
        self.ativo.setGeometry(QtCore.QRect(160, 100, 113, 20))
        self.ativo.setObjectName(_fromUtf8("ativo"))
        self.label_2 = QtGui.QLabel(pag_F)
        self.label_2.setGeometry(QtCore.QRect(290, 100, 111, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.salario = QtGui.QLabel(pag_F)
        self.salario.setGeometry(QtCore.QRect(70, 200, 61, 16))
        self.salario.setObjectName(_fromUtf8("salario"))
        self.aluguel = QtGui.QLabel(pag_F)
        self.aluguel.setGeometry(QtCore.QRect(70, 240, 47, 13))
        self.aluguel.setObjectName(_fromUtf8("aluguel"))
        self.acoes = QtGui.QLabel(pag_F)
        self.acoes.setGeometry(QtCore.QRect(70, 280, 47, 13))
        self.acoes.setObjectName(_fromUtf8("acoes"))
        self.salario_ativo = QtGui.QLineEdit(pag_F)
        self.salario_ativo.setGeometry(QtCore.QRect(160, 200, 113, 21))
        self.salario_ativo.setText(_fromUtf8(""))
        self.salario_ativo.setObjectName(_fromUtf8("salario_ativo"))
        self.aluguel_ativo = QtGui.QLineEdit(pag_F)
        self.aluguel_ativo.setGeometry(QtCore.QRect(160, 240, 113, 20))
        self.aluguel_ativo.setObjectName(_fromUtf8("aluguel_ativo"))
        self.acoes_ativo = QtGui.QLineEdit(pag_F)
        self.acoes_ativo.setGeometry(QtCore.QRect(160, 280, 113, 20))
        self.acoes_ativo.setObjectName(_fromUtf8("acoes_ativo"))
        self.adicionar_categoria = QtGui.QPushButton(pag_F)
        self.adicionar_categoria.setGeometry(QtCore.QRect(30, 370, 141, 23))
        self.adicionar_categoria.setObjectName(_fromUtf8("adicionar_categoria"))
        self.voltar = QtGui.QPushButton(pag_F)
        self.voltar.setGeometry(QtCore.QRect(230, 370, 75, 23))
        self.voltar.setObjectName(_fromUtf8("voltar"))
        self.total = QtGui.QLabel(pag_F)
        self.total.setGeometry(QtCore.QRect(70, 330, 47, 16))
        self.total.setObjectName(_fromUtf8("total"))
        self.total_ativo = QtGui.QLineEdit(pag_F)
        self.total_ativo.setGeometry(QtCore.QRect(160, 330, 113, 20))
        self.total_ativo.setObjectName(_fromUtf8("total_ativo"))
        self.categorias = QtGui.QComboBox(pag_F)
        self.categorias.setGeometry(QtCore.QRect(160, 60, 111, 22))
        self.categorias.setObjectName(_fromUtf8("categorias"))
        self.categorias.addItem(_fromUtf8(""))
        self.categorias.setItemText(0, _fromUtf8(""))
        self.categorias.addItem(_fromUtf8(""))
        self.categorias.addItem(_fromUtf8(""))
        self.categorias.addItem(_fromUtf8(""))
        self.categorias.addItem(_fromUtf8(""))
        self.categoria = QtGui.QLabel(pag_F)
        self.categoria.setGeometry(QtCore.QRect(70, 60, 71, 16))
        self.categoria.setObjectName(_fromUtf8("categoria"))

        self.retranslateUi(pag_F)
        QtCore.QMetaObject.connectSlotsByName(pag_F)

    def retranslateUi(self, pag_F):
        pag_F.setWindowTitle(_translate("pag_F", "Dialog", None))
        self.ativos.setText(_translate("pag_F", "ATIVOS", None))
        self.adicionar_ativo.setText(_translate("pag_F", "ADICIONAR ATIVO", None))
        self.label_2.setText(_translate("pag_F", "EX: R$15,30 = 15,30", None))
        self.salario.setText(_translate("pag_F", "SALÁRIO", None))
        self.aluguel.setText(_translate("pag_F", "ALUGUEL", None))
        self.acoes.setText(_translate("pag_F", "AÇÕES", None))
        self.adicionar_categoria.setText(_translate("pag_F", "ADICIONAR CATEGORIA", None))
        self.voltar.setText(_translate("pag_F", "VOLTAR", None))
        self.total.setText(_translate("pag_F", "TOTAL", None))
        self.categorias.setItemText(1, _translate("pag_F", "Aluguel", None))
        self.categorias.setItemText(2, _translate("pag_F", "Ações", None))
        self.categorias.setItemText(3, _translate("pag_F", "Salário", None))
        self.categorias.setItemText(4, _translate("pag_F", "Poupança", None))
        self.categoria.setText(_translate("pag_F", "CATEGORIA", None))

