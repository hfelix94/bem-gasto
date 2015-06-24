# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G.ui'
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

class Ui_pag_G(object):
    def setupUi(self, pag_G):
        pag_G.setObjectName(_fromUtf8("pag_G"))
        pag_G.resize(467, 435)
        self.passivos = QtGui.QLabel(pag_G)
        self.passivos.setGeometry(QtCore.QRect(30, 20, 61, 16))
        self.passivos.setObjectName(_fromUtf8("passivos"))
        self.adicionar_passivo = QtGui.QPushButton(pag_G)
        self.adicionar_passivo.setGeometry(QtCore.QRect(180, 120, 121, 23))
        self.adicionar_passivo.setObjectName(_fromUtf8("adicionar_passivo"))
        self.passivo = QtGui.QLineEdit(pag_G)
        self.passivo.setGeometry(QtCore.QRect(180, 90, 121, 20))
        self.passivo.setObjectName(_fromUtf8("passivo"))
        self.exemplo_passivos = QtGui.QLabel(pag_G)
        self.exemplo_passivos.setGeometry(QtCore.QRect(310, 90, 111, 16))
        self.exemplo_passivos.setObjectName(_fromUtf8("exemplo_passivos"))
        self.aluguel = QtGui.QLabel(pag_G)
        self.aluguel.setGeometry(QtCore.QRect(60, 190, 61, 16))
        self.aluguel.setObjectName(_fromUtf8("aluguel"))
        self.luz = QtGui.QLabel(pag_G)
        self.luz.setGeometry(QtCore.QRect(60, 230, 47, 13))
        self.luz.setObjectName(_fromUtf8("luz"))
        self.telefone = QtGui.QLabel(pag_G)
        self.telefone.setGeometry(QtCore.QRect(60, 270, 61, 16))
        self.telefone.setObjectName(_fromUtf8("telefone"))
        self.aluguel_passivos = QtGui.QLineEdit(pag_G)
        self.aluguel_passivos.setGeometry(QtCore.QRect(180, 190, 121, 20))
        self.aluguel_passivos.setObjectName(_fromUtf8("aluguel_passivos"))
        self.categoria = QtGui.QLabel(pag_G)
        self.categoria.setGeometry(QtCore.QRect(60, 60, 71, 16))
        self.categoria.setObjectName(_fromUtf8("categoria"))
        self.categoria_passivos = QtGui.QComboBox(pag_G)
        self.categoria_passivos.setGeometry(QtCore.QRect(180, 60, 121, 22))
        self.categoria_passivos.setObjectName(_fromUtf8("categoria_passivos"))
        self.categoria_passivos.addItem(_fromUtf8(""))
        self.categoria_passivos.setItemText(0, _fromUtf8(""))
        self.categoria_passivos.addItem(_fromUtf8(""))
        self.categoria_passivos.addItem(_fromUtf8(""))
        self.categoria_passivos.addItem(_fromUtf8(""))
        self.categoria_passivos.addItem(_fromUtf8(""))
        self.categoria_passivos.addItem(_fromUtf8(""))
        self.luz_passivos = QtGui.QLineEdit(pag_G)
        self.luz_passivos.setGeometry(QtCore.QRect(180, 230, 121, 20))
        self.luz_passivos.setObjectName(_fromUtf8("luz_passivos"))
        self.telefone_passivos = QtGui.QLineEdit(pag_G)
        self.telefone_passivos.setGeometry(QtCore.QRect(180, 270, 121, 20))
        self.telefone_passivos.setObjectName(_fromUtf8("telefone_passivos"))
        self.total = QtGui.QLabel(pag_G)
        self.total.setGeometry(QtCore.QRect(60, 330, 47, 13))
        self.total.setObjectName(_fromUtf8("total"))
        self.total_passivos = QtGui.QLineEdit(pag_G)
        self.total_passivos.setGeometry(QtCore.QRect(180, 330, 121, 20))
        self.total_passivos.setObjectName(_fromUtf8("total_passivos"))
        self.adicionar_categoria_passivos = QtGui.QPushButton(pag_G)
        self.adicionar_categoria_passivos.setGeometry(QtCore.QRect(60, 400, 131, 23))
        self.adicionar_categoria_passivos.setObjectName(_fromUtf8("adicionar_categoria_passivos"))
        self.voltar = QtGui.QPushButton(pag_G)
        self.voltar.setGeometry(QtCore.QRect(250, 400, 75, 23))
        self.voltar.setObjectName(_fromUtf8("voltar"))

        self.retranslateUi(pag_G)
        QtCore.QMetaObject.connectSlotsByName(pag_G)

    def retranslateUi(self, pag_G):
        pag_G.setWindowTitle(_translate("pag_G", "Dialog", None))
        self.passivos.setText(_translate("pag_G", "PASSIVOS", None))
        self.adicionar_passivo.setText(_translate("pag_G", "ADICIONAR PASSIVO", None))
        self.exemplo_passivos.setText(_translate("pag_G", "EX: R$15,30 = 15,30", None))
        self.aluguel.setText(_translate("pag_G", "ALUGUEL", None))
        self.luz.setText(_translate("pag_G", "LUZ", None))
        self.telefone.setText(_translate("pag_G", "TELEFONE", None))
        self.categoria.setText(_translate("pag_G", "CATEGORIA", None))
        self.categoria_passivos.setItemText(1, _translate("pag_G", "Alimentação", None))
        self.categoria_passivos.setItemText(2, _translate("pag_G", "Aluguel", None))
        self.categoria_passivos.setItemText(3, _translate("pag_G", "Luz", None))
        self.categoria_passivos.setItemText(4, _translate("pag_G", "Telefone", None))
        self.categoria_passivos.setItemText(5, _translate("pag_G", "Transporte", None))
        self.total.setText(_translate("pag_G", "TOTAL", None))
        self.adicionar_categoria_passivos.setText(_translate("pag_G", "ADICIONAR CATEGORIA", None))
        self.voltar.setText(_translate("pag_G", "VOLTAR", None))

