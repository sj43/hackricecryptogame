# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/williamyam/Documents/GitHub/hackricecryptogame/GameWindowScreen/investment_window.ui',
# licensing of '/Users/williamyam/Documents/GitHub/hackricecryptogame/GameWindowScreen/investment_window.ui' applies.
#
# Created: Sat Mar  2 14:15:11 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(960, 600)
        self.Title = QtWidgets.QTextBrowser(Dialog)
        self.Title.setGeometry(QtCore.QRect(110, 30, 721, 100))
        self.Title.setObjectName("Title")
        self.stock_low_button = QtWidgets.QPushButton(Dialog)
        self.stock_low_button.setGeometry(QtCore.QRect(109, 160, 241, 200))
        self.stock_low_button.setObjectName("stock_low_button")
        self.stock_high_button = QtWidgets.QPushButton(Dialog)
        self.stock_high_button.setGeometry(QtCore.QRect(590, 160, 241, 200))
        self.stock_high_button.setObjectName("stock_high_button")
        self.fixed_3_button = QtWidgets.QPushButton(Dialog)
        self.fixed_3_button.setGeometry(QtCore.QRect(109, 360, 241, 200))
        self.fixed_3_button.setObjectName("fixed_3_button")
        self.stock_avg_button = QtWidgets.QPushButton(Dialog)
        self.stock_avg_button.setGeometry(QtCore.QRect(350, 160, 241, 200))
        self.stock_avg_button.setObjectName("stock_avg_button")
        self.fixed_6_button = QtWidgets.QPushButton(Dialog)
        self.fixed_6_button.setGeometry(QtCore.QRect(350, 360, 241, 200))
        self.fixed_6_button.setObjectName("fixed_6_button")
        self.fixed_12_button = QtWidgets.QPushButton(Dialog)
        self.fixed_12_button.setGeometry(QtCore.QRect(590, 360, 241, 200))
        self.fixed_12_button.setObjectName("fixed_12_button")
        self.back_button = QtWidgets.QPushButton(Dialog)
        self.back_button.setGeometry(QtCore.QRect(840, 511, 91, 51))
        self.back_button.setObjectName("back_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.Title.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Gulim\'; font-size:48pt;\">INVESTMENTS</span></p></body></html>", None, -1))
        self.stock_low_button.setText(QtWidgets.QApplication.translate("Dialog", "Low-risk Stock", None, -1))
        self.stock_high_button.setText(QtWidgets.QApplication.translate("Dialog", "High-risk Stock", None, -1))
        self.fixed_3_button.setText(QtWidgets.QApplication.translate("Dialog", "3-month Fixed Savings", None, -1))
        self.stock_avg_button.setText(QtWidgets.QApplication.translate("Dialog", "Average-risk Stock", None, -1))
        self.fixed_6_button.setText(QtWidgets.QApplication.translate("Dialog", "6-month Fixed Savings", None, -1))
        self.fixed_12_button.setText(QtWidgets.QApplication.translate("Dialog", "12-month Fixed Savings", None, -1))
        self.back_button.setText(QtWidgets.QApplication.translate("Dialog", "Back", None, -1))

