import sys

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QFile, QObject, Signal, Slot


class PropertyWindow(QObject):

    buy_property = Signal(int)

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

        back_button.clicked.connect(self.close_window)
        estate_apartment_button.clicked.connect(self.buy_estate_apartment)
        estate_house_button.clicked.connect(self.buy_estate_house)
        estate_penthouse_button.clicked.connect(self.buy_estate_penthouse)
        vehicle_economy_button.clicked.connect(self.buy_vehicle_economy)
        vehicle_middle_button.clicked.connect(self.buy_vehicle_middle)
        vehicle_luxury_button.clicked.connect(self.buy_vehicle_luxury)

        self.window.show()

    def close_window(self):
        self.window.hide()

    def buy_stock_low(self):
        self.make_investment.emit(1)
        self.window.hide()

    def buy_stock_avg(self):
        self.make_investment.emit(2)
        self.window.hide()

    def buy_stock_high(self):
        self.make_investment.emit(3)
        self.window.hide()

    def buy_fixed_3(self):
        self.make_investment.emit(4)
        self.window.hide()

    def buy_fixed_6(self):
        self.make_investment.emit(5)
        self.window.hide()

    def buy_fixed_12(self):
        self.make_investment.emit(6)
        self.window.hide()


class InvestmentWindow(QObject):

    make_investment = Signal(int)

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

        back_button.clicked.connect(self.close_window)
        stock_low_button.clicked.connect(self.buy_stock_low)
        stock_avg_button.clicked.connect(self.buy_stock_avg)
        stock_high_button.clicked.connect(self.buy_stock_high)
        fixed_3_button.clicked.connect(self.buy_fixed_3)
        fixed_6_button.clicked.connect(self.buy_fixed_6)
        fixed_12_button.clicked.connect(self.buy_fixed_12())

        self.window.show()

    def close_window(self):
        self.window.hide()

    def buy_stock_low(self):
        self.buy_investment.emit(1)
        self.window.hide()

    def buy_stock_avg(self):
        self.buy_investment.emit(2)
        self.window.hide()

    def buy_stock_high(self):
        self.buy_investment.emit(3)
        self.window.hide()

    def buy_fixed_3(self):
        self.buy_investment.emit(4)
        self.window.hide()

    def buy_fixed_6(self):
        self.buy_investment.emit(5)
        self.window.hide()

    def buy_fixed_12(self):
        self.buy_investment.emit(6)
        self.window.hide()


app = QApplication(sys.argv)
form = PropertyWindow('property_window.ui')
sys.exit(app.exec_())
