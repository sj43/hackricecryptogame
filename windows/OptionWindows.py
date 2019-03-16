import sys

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton, QListWidget
from PySide2.QtCore import QFile, QObject, Signal, Slot

class CryptoWindow(QObject):

    buy_crypto = Signal(int)
    sell_crypto = Signal(int)

    def __init__(self, ui_file, parent=None):
        super(CryptoWindow, self).__init__(parent)
        self.window = QUiLoader().load(ui_file)
        self.extract_buttons()
        self.connect_signals()
        self.window.hide()

    def extract_buttons(self):
        self.back_button = self.window.findChild(QPushButton, 'back_button')
        self.buy_button_1 = self.window.findChild(QPushButton, 'buy_button_1')
        self.buy_button_2 = self.window.findChild(QPushButton, 'buy_button_2')
        self.buy_button_3 = self.window.findChild(QPushButton, 'buy_button_3')
        self.buy_button_4 = self.window.findChild(QPushButton, 'buy_button_4')
        self.buy_button_5 = self.window.findChild(QPushButton, 'buy_button_5')
        self.buy_button_6 = self.window.findChild(QPushButton, 'buy_button_6')
        self.sell_button_1 = self.window.findChild(QPushButton, 'sell_button_1')
        self.sell_button_2 = self.window.findChild(QPushButton, 'sell_button_2')
        self.sell_button_3 = self.window.findChild(QPushButton, 'sell_button_3')
        self.sell_button_4 = self.window.findChild(QPushButton, 'sell_button_4')
        self.sell_button_5 = self.window.findChild(QPushButton, 'sell_button_5')
        self.sell_button_6 = self.window.findChild(QPushButton, 'sell_button_6')

    def connect_signals(self):
        self.back_button.clicked.connect(self.close_window)
        self.buy_button_1.clicked.connect(self.buy_crypto_1)
        self.buy_button_2.clicked.connect(self.buy_crypto_2)
        self.buy_button_3.clicked.connect(self.buy_crypto_3)
        self.buy_button_4.clicked.connect(self.buy_crypto_4)
        self.buy_button_5.clicked.connect(self.buy_crypto_5)
        self.buy_button_6.clicked.connect(self.buy_crypto_6)
        self.sell_button_1.clicked.connect(self.sell_crypto_1)
        self.sell_button_2.clicked.connect(self.sell_crypto_2)
        self.sell_button_3.clicked.connect(self.sell_crypto_3)
        self.sell_button_4.clicked.connect(self.sell_crypto_4)
        self.sell_button_5.clicked.connect(self.sell_crypto_5)
        self.sell_button_6.clicked.connect(self.sell_crypto_6)

    def open_window(self):
        self.window.show()

    def close_window(self):
        self.window.hide()

    def buy_crypto_1(self):
        self.buy_crypto.emit(1)
        self.window.hide()

    def buy_crypto_2(self):
        self.buy_crypto.emit(2)
        self.window.hide()

    def buy_crypto_3(self):
        self.buy_crypto.emit(3)
        self.window.hide()

    def buy_crypto_4(self):
        self.buy_crypto.emit(4)
        self.window.hide()

    def buy_crypto_5(self):
        self.buy_crypto.emit(5)
        self.window.hide()

    def buy_crypto_6(self):
        self.buy_crypto.emit(6)
        self.window.hide()

    def sell_crypto_1(self):
        self.sell_crypto.emit(1)
        self.window.hide()

    def sell_crypto_2(self):
        self.sell_crypto.emit(2)
        self.window.hide()

    def sell_crypto_3(self):
        self.sell_crypto.emit(3)
        self.window.hide()

    def sell_crypto_4(self):
        self.sell_crypto.emit(4)
        self.window.hide()

    def sell_crypto_5(self):
        self.sell_crypto.emit(5)
        self.window.hide()

    def sell_crypto_6(self):
        self.sell_crypto.emit(6)
        self.window.hide()


class PropertyWindow(QObject):

    buy_property = Signal(int)

    def __init__(self, ui_file, parent=None):
        super(PropertyWindow, self).__init__(parent)
        self.window = QUiLoader().load(ui_file)
        self.extract_buttons()
        self.connect_signals()
        self.window.hide()

    def extract_buttons(self):
        self.back_button = self.window.findChild(QPushButton, 'back_button')
        self.estate_apartment_button = self.window.findChild(QPushButton, 'estate_apartment_button')
        self.estate_house_button = self.window.findChild(QPushButton, 'estate_house_button')
        self.estate_penthouse_button = self.window.findChild(QPushButton, 'estate_penthouse_button')
        self.vehicle_economy_button = self.window.findChild(QPushButton, 'vehicle_economy_button')
        self.vehicle_middle_button = self.window.findChild(QPushButton, 'vehicle_middle_button')
        self.vehicle_luxury_button = self.window.findChild(QPushButton, 'vehicle_luxury_button')

    def connect_signals(self):
        self.back_button.clicked.connect(self.close_window)
        self.estate_apartment_button.clicked.connect(self.buy_estate_apartment)
        self.estate_house_button.clicked.connect(self.buy_estate_house)
        self.estate_penthouse_button.clicked.connect(self.buy_estate_penthouse)
        self.vehicle_economy_button.clicked.connect(self.buy_vehicle_economy)
        self.vehicle_middle_button.clicked.connect(self.buy_vehicle_middle)
        self.vehicle_luxury_button.clicked.connect(self.buy_vehicle_luxury)

    def open_window(self):
        self.window.show()

    def close_window(self):
        self.window.hide()

    def buy_estate_apartment(self):
        self.buy_property.emit(1)
        self.window.hide()

    def buy_estate_house(self):
        self.buy_property.emit(2)
        self.window.hide()

    def buy_estate_penthouse(self):
        self.buy_property.emit(3)
        self.window.hide()

    def buy_vehicle_economy(self):
        self.buy_property.emit(4)
        self.window.hide()

    def buy_vehicle_middle(self):
        self.buy_property.emit(5)
        self.window.hide()

    def buy_vehicle_luxury(self):
        self.buy_property.emit(6)
        self.window.hide()


class InvestmentWindow(QObject):

    make_investment = Signal(int)

    def __init__(self, ui_file, parent=None):
        super(InvestmentWindow, self).__init__(parent)
        self.window = QUiLoader().load(ui_file)
        self.extract_buttons()
        self.connect_signals()
        self.window.hide()

    def extract_buttons(self):
        self.back_button = self.window.findChild(QPushButton, 'back_button')
        self.stock_low_button = self.window.findChild(QPushButton, 'stock_low_button')
        self.stock_avg_button = self.window.findChild(QPushButton, 'stock_avg_button')
        self.stock_high_button = self.window.findChild(QPushButton, 'stock_high_button')
        self.fixed_3_button = self.window.findChild(QPushButton, 'fixed_3_button')
        self.fixed_6_button = self.window.findChild(QPushButton, 'fixed_6_button')
        self.fixed_12_button = self.window.findChild(QPushButton, 'fixed_12_button')

    def connect_signals(self):
        self.back_button.clicked.connect(self.close_window)
        self.stock_low_button.clicked.connect(self.buy_stock_low)
        self.stock_avg_button.clicked.connect(self.buy_stock_avg)
        self.stock_high_button.clicked.connect(self.buy_stock_high)
        self.fixed_3_button.clicked.connect(self.buy_fixed_3)
        self.fixed_6_button.clicked.connect(self.buy_fixed_6)
        self.fixed_12_button.clicked.connect(self.buy_fixed_12)

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


class BankWindow(QObject):

    get_loan = Signal(int)

    def __init__(self, ui_file, parent=None):
        super(BankWindow, self).__init__(parent)

        self.window = QUiLoader().load(ui_file)
        self.extract_buttons()
        self.connect_signals()
        self.window.hide()

    def extract_buttons(self):
        self.interest_list = self.window.findChild(QListWidget, 'interest_list')
        self.back_button = self.window.findChild(QPushButton, 'back_button')
        self.loan_100_button = self.window.findChild(QPushButton, 'loan_100_button')
        self.loan_30_button = self.window.findChild(QPushButton, 'loan_30_button')
        self.loan_10_button = self.window.findChild(QPushButton, 'loan_10_button')

    def connect_signals(self):
        self.back_button.clicked.connect(self.close_window)
        self.loan_100_button.clicked.connect(self.loan_100)
        self.loan_30_button.clicked.connect(self.loan_30)
        self.loan_10_button.clicked.connect(self.loan_10)

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

    open_crypto = Signal()
    open_property = Signal()
    open_investment = Signal()
    open_bank = Signal()

    living_expenses = Signal(int)
    card_repay = Signal(int)

    end_turn_signal = Signal()

    def __init__(self, ui_file, parent=None):
        super(MainWindow, self).__init__(parent)

        self.window = QUiLoader().load(ui_file)
        self.extract_buttons()
        self.connect_signals()
        self.window.show()

        self.fee_payment_list = self.window.findChild(QListWidget, 'fee_payment')

    def extract_buttons(self):
        self.bank_button = self.window.findChild(QPushButton, 'BankButton')
        self.crypto_button = self.window.findChild(QPushButton, 'CryptoButton')
        self.property_button = self.window.findChild(QPushButton, 'PropertyButton')
        self.investment_button = self.window.findChild(QPushButton, 'InvestmentButton')

        self.end_turn_button = self.window.findChild(QPushButton, 'end_turn')

        self.living_card_button = self.window.findChild(QPushButton, 'living_card')
        self.living_savings_button = self.window.findChild(QPushButton, 'living_savings')
        self.card_repay_button = self.window.findChild(QPushButton, 'card_repay')
        self.card_notrepay_button = self.window.findChild(QPushButton, 'card_notrepay')

    def connect_signals(self):
        self.bank_button.clicked.connect(self.open_bank_window)
        self.crypto_button.clicked.connect(self.open_crypto_window)
        self.property_button.clicked.connect(self.open_property_window)
        self.investment_button.clicked.connect(self.open_investment_window)

        self.living_card_button.clicked.connect(self.living_expenses_card)
        self.living_savings_button.clicked.connect(self.living_expenses_savings)
        self.card_repay_button.clicked.connect(self.credit_card_repay)
        self.card_notrepay_button.clicked.connect(self.credit_card_notrepay)

        self.end_turn_button.clicked.connect(self.end_turn)

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

    def end_turn(self):
        self.end_turn_signal.emit()

