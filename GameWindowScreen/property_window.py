# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/williamyam/Documents/GitHub/hackricecryptogame/GameWindowScreen/property_window.ui',
# licensing of '/Users/williamyam/Documents/GitHub/hackricecryptogame/GameWindowScreen/property_window.ui' applies.
#
# Created: Sat Mar  2 14:11:15 2019
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
        self.vehicle_economy_button = QtWidgets.QPushButton(Dialog)
        self.vehicle_economy_button.setGeometry(QtCore.QRect(109, 160, 241, 200))
        self.vehicle_economy_button.setObjectName("vehicle_economy_button")
        self.vehicle_luxury_button = QtWidgets.QPushButton(Dialog)
        self.vehicle_luxury_button.setGeometry(QtCore.QRect(590, 160, 241, 200))
        self.vehicle_luxury_button.setObjectName("vehicle_luxury_button")
        self.estate_apartment_button = QtWidgets.QPushButton(Dialog)
        self.estate_apartment_button.setGeometry(QtCore.QRect(109, 360, 241, 200))
        self.estate_apartment_button.setObjectName("estate_apartment_button")
        self.vehicle_middle_button = QtWidgets.QPushButton(Dialog)
        self.vehicle_middle_button.setGeometry(QtCore.QRect(350, 160, 241, 200))
        self.vehicle_middle_button.setObjectName("vehicle_middle_button")
        self.estate_house_button = QtWidgets.QPushButton(Dialog)
        self.estate_house_button.setGeometry(QtCore.QRect(350, 360, 241, 200))
        self.estate_house_button.setObjectName("estate_house_button")
        self.estate_penthouse_button = QtWidgets.QPushButton(Dialog)
        self.estate_penthouse_button.setGeometry(QtCore.QRect(590, 360, 241, 200))
        self.estate_penthouse_button.setObjectName("estate_penthouse_button")
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
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Gulim\'; font-size:48pt;\">PROPERTIES</span></p></body></html>", None, -1))
        self.vehicle_economy_button.setText(QtWidgets.QApplication.translate("Dialog", "Economy Vehicle", None, -1))
        self.vehicle_luxury_button.setText(QtWidgets.QApplication.translate("Dialog", "Luxury Vehicle", None, -1))
        self.estate_apartment_button.setText(QtWidgets.QApplication.translate("Dialog", "Apartment Real Estate", None, -1))
        self.vehicle_middle_button.setText(QtWidgets.QApplication.translate("Dialog", "Middle Vehicle", None, -1))
        self.estate_house_button.setText(QtWidgets.QApplication.translate("Dialog", "House Real Estate", None, -1))
        self.estate_penthouse_button.setText(QtWidgets.QApplication.translate("Dialog", "Penthouse Real Estate", None, -1))
        self.back_button.setText(QtWidgets.QApplication.translate("Dialog", "Back", None, -1))

