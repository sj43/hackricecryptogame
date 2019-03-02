import sys

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QFile, QObject


class InvestmentWindow(QObject):

    def __init__(self, ui_file, parent=None):
        super(InvestmentWindow, self).__init__(parent)
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()

        back_button = self.window.findChild(QPushButton, 'back_button')
        stock_low_button = self.window.findChild(QPushButton, 'stock_low_button')
        stock_avg_button = self.window.findChild(QPushButton, 'stock_avg_button')
        stock_high_button = self.window.findChild(QPushButton, 'stock_high_button')
        fixed_3_button = self.window.findChild(QPushButton, 'fixed_3_button')
        fixed_6_button = self.window.findChild(QPushButton, 'fixed_6_button')
        fixed_12_button = self.window.findChild(QPushButton, 'fixed_12_button')

        back_button.clicked.connect(self.ok_handler)
        stock_low_button.clicked.connect(self.ok_handler)
        stock_avg_button.clicked.connect(self.ok_handler)
        stock_high_button.clicked.connect(self.ok_handler)
        fixed_3_button.clicked.connect(self.ok_handler)
        fixed_6_button.clicked.connect(self.ok_handler)
        fixed_12_button.clicked.connect(self.ok_handler)

        self.window.show()

    def ok_handler(self):
        print('works!')


class PropertyWindow(QObject):

    def __init__(self, ui_file, parent=None):
        super(PropertyWindow, self).__init__(parent)
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()

        back_button = self.window.findChild(QPushButton, 'back_button')
        estate_apartment_button = self.window.findChild(QPushButton, 'estate_apartment_button')
        estate_house_button = self.window.findChild(QPushButton, 'estate_house_button')
        estate_penthouse_button = self.window.findChild(QPushButton, 'estate_penthouse_button')
        vehicle_economy_button = self.window.findChild(QPushButton, 'vehicle_economy_button')
        vehicle_middle_button = self.window.findChild(QPushButton, 'vehicle_middle_button')
        vehicle_luxury_button = self.window.findChild(QPushButton, 'vehicle_luxury_button')

        back_button.clicked.connect(self.ok_handler)
        estate_apartment_button.clicked.connect(self.ok_handler)
        estate_house_button.clicked.connect(self.ok_handler)
        estate_penthouse_button.clicked.connect(self.ok_handler)
        vehicle_economy_button.clicked.connect(self.ok_handler)
        vehicle_middle_button.clicked.connect(self.ok_handler)
        vehicle_luxury_button.clicked.connect(self.ok_handler)

        self.window.show()

    def ok_handler(self):
        print('works!')


app = QApplication(sys.argv)
form = PropertyWindow('property_window.ui')
sys.exit(app.exec_())
