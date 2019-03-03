import sys

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton, QListWidget
from PySide2.QtCore import QFile, QObject, Signal, Slot


class PropertyWindow(QObject):

    buy_property = Signal(int)

    def __init__(self, ui_file, parent=None):
        super(PropertyWindow, self).__init__(parent)
        app = QApplication(sys.argv)
        self.window = QUiLoader().load(ui_file)

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

        self.window.hide()
        sys.exit(app.exec_())

    def open_window(self):
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
        app = QApplication(sys.argv)
        self.window = QUiLoader().load(ui_file)

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

        self.window.hide()
        sys.exit(app.exec_())

    def open_window(self):
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


class BankWindow(QObject):

    get_loan = Signal(int)

    def __init__(self, ui_file, parent=None):
        super(BankWindow, self).__init__(parent)

        app = QApplication(sys.argv)
        self.window = QUiLoader().load(ui_file)
        self.connect_signals()
        self.window.show()
        sys.exit(app.exec_())

    def connect_signals(self):
        interest_list = self.window.findChild(QListWidget, 'interest_list')
        back_button = self.window.findChild(QPushButton, 'back_button')
        loan_100_button = self.window.findChild(QPushButton, 'loan_100_button')
        loan_30_button = self.window.findChild(QPushButton, 'loan_30_button')
        loan_10_button = self.window.findChild(QPushButton, 'loan_10_button')

        back_button.clicked.connect(self.close_window)
        loan_100_button.clicked.connect(self.loan_100)
        loan_30_button.clicked.connect(self.loan_30)
        loan_10_button.clicked.connect(self.loan_10)

    def open_window(self):
        self.window.show()

    def close_window(self):
        self.window.hide()

    def set_loan_amount(self, maxLoanAmount, loanInterest):
        self.interest_list.clear()
        self.interest_list.addItem(str("Max Loan Amount: ") + str(maxLoanAmount))
        self.interest_list.addItem(str("Loan Interest: ") + str(loanInterest))

    def loan_100(self):
        self.get_loan.emit(1.0)
        self.window.hide()

    def loan_30(self):
        self.get_loan.emit(0.3)
        self.window.hide()

    def loan_10(self):
        self.get_loan.emit(0.1)
        self.window.hide()


class MainWindow(QObject):

    open_bank = Signal()
    open_crypto = Signal()
    open_property = Signal()
    open_investment = Signal()

    living_expenses = Signal(int)
    card_repay = Signal(int)

    def __init__(self, ui_file, parent=None):
        super(MainWindow, self).__init__(parent)

        app = QApplication(sys.argv)
        self.window = QUiLoader().load(ui_file)
        self.connect_signals()
        self.window.show()
        sys.exit(app.exec_())

    def connect_signals(self):
        bank_button = self.window.findChild(QPushButton, 'BankButton')
        crypto_button = self.window.findChild(QPushButton, 'CryptoButton')
        property_button = self.window.findChild(QPushButton, 'PropertyButton')
        investment_button = self.window.findChild(QPushButton, 'InvestmentButton')

        living_card_button = self.window.findChild(QPushButton, 'living_card')
        living_savings_button = self.window.findChild(QPushButton, 'living_savings')
        card_repay_button = self.window.findChild(QPushButton, 'card_repay')
        card_notrepay_button = self.window.findChild(QPushButton, 'card_notrepay')

        fee_payment_list = self.window.findChild(QListWidget, 'fee_payment')

        bank_button.clicked.connect(self.open_bank_window)
        crypto_button.clicked.connect(self.open_crypto_window)
        property_button.clicked.connect(self.open_property_window)
        investment_button.clicked.connect(self.open_investment_window)

        living_card_button.clicked.connect(self.living_expenses_card)
        living_savings_button.clicked.connect(self.living_expenses_savings)
        card_repay_button.clicked.connect(self.credit_card_repay)
        card_notrepay_button.clicked.connect(self.credit_card_notrepay)

    def open_window(self):
        self.window.show()

    def close_window(self):
        self.window.hide()

    def open_bank_window(self):
        self.open_bank.emit()

    def open_crypto_window(self):
        self.open_crypto.emit()

    def open_property_window(self):
        self.open_property.emit()

    def open_investment_window(self):
        self.open_investment.emit()

    def living_expenses_card(self):
        self.living_expenses.emit(1)

    def living_expenses_savings(self):
        self.living_expenses.emit(2)

    def credit_card_repay(self):
        self.card_repay.emit(1)

    def credit_card_notrepay(self):
        self.card_repay.emit(2)

    def display_fee_payment(self, payment):
        self.fee_payment_list.addItem(payment)


MainWindow("main_window.ui")
BankWindow("bank_window.ui")
