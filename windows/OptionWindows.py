import sys

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton, QListWidget
from PySide2.QtCore import QFile, QObject, Signal, Slot

import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QObject, Signal, Slot

from GameFunctions import *
##from windows.OptionWindows import *
from classes.quest import *


##from Crypto.market import *


class PropertyWindow(QObject):

    buy_property = Signal(int)

    def __init__(self, ui_file, parent=None):
        super(PropertyWindow, self).__init__(parent)
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
        self.connect_signals()
        self.window.hide()

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

    end_turn_signal = Signal()

    def __init__(self, ui_file, parent=None):
        super(MainWindow, self).__init__(parent)

        self.window = QUiLoader().load(ui_file)
        self.connect_signals()
        self.window.show()

        self.fee_payment_list = self.window.findChild(QListWidget, 'fee_payment')

    def connect_signals(self):
        bank_button = self.window.findChild(QPushButton, 'BankButton')
        crypto_button = self.window.findChild(QPushButton, 'CryptoButton')
        property_button = self.window.findChild(QPushButton, 'PropertyButton')
        investment_button = self.window.findChild(QPushButton, 'InvestmentButton')

        end_turn_button = self.window.findChild(QPushButton, 'end_turn')

        living_card_button = self.window.findChild(QPushButton, 'living_card')
        living_savings_button = self.window.findChild(QPushButton, 'living_savings')
        card_repay_button = self.window.findChild(QPushButton, 'card_repay')
        card_notrepay_button = self.window.findChild(QPushButton, 'card_notrepay')

        bank_button.clicked.connect(self.open_bank_window)
        crypto_button.clicked.connect(self.open_crypto_window)
        property_button.clicked.connect(self.open_property_window)
        investment_button.clicked.connect(self.open_investment_window)

        living_card_button.clicked.connect(self.living_expenses_card)
        living_savings_button.clicked.connect(self.living_expenses_savings)
        card_repay_button.clicked.connect(self.credit_card_repay)
        card_notrepay_button.clicked.connect(self.credit_card_notrepay)

        end_turn_button.clicked.connect(self.end_turn)

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


##MainWindow("main_window.ui")
##BankWindow("bank_window.ui")


class GameInstance(GameFunctions):
    """Game instance """

    def __init__(self, startDate):
        GameFunctions.__init__(self, startDate)

        app = QApplication(sys.argv)
        self.MainWindow = MainWindow("main_window.ui")
        self.PropertyWindow = PropertyWindow('property_window.ui')
        self.InvestmentWindow = InvestmentWindow('investment_window.ui')
        self.BankWindow = BankWindow('bank_window.ui')
        self.connect_signals_and_slots()
        sys.exit(app.exec_())


    def connect_signals_and_slots(self):
        self.MainWindow.open_bank.connect(self.player_ask_loan)
        ##MainWindow.open_crypto.connect(CryptoWindow.open_window)
        self.MainWindow.open_property.connect(self.player_ask_property)
        self.MainWindow.open_investment.connect(self.player_ask_investment)

        self.PropertyWindow.buy_property.connect(self.player_buy_property)
        self.InvestmentWindow.make_investment.connect(self.player_make_investment)
        self.BankWindow.get_loan.connect(self.player_get_loan)

        self.max_loan_amount.connect(self.BankWindow.set_loan_amount)
        #self.see_loan.connect(self.BankWindow.open_window)

        self.see_property.connect(self.PropertyWindow.open_window)
        self.see_investment.connect(self.InvestmentWindow.open_window)

        self.MainWindow.living_expenses.connect(self.choice_living_expenses)
        self.MainWindow.card_repay.connect(self.choice_card)
        ##self.show_payment.connect(self.MainWindow.display_fee_payment())

        self.MainWindow.end_turn_signal.connect(self.end_turn)

    def player_action(self):
        pass

    def get_date(self):
        return self.date

    @Slot()
    def end_turn(self):
        # update player info

        self.get_income()

        # show quest here (1. only when there is no existing quest, 2. not always create a quest)
        """
        if self.my_quest == None:
            if random.randint(0, 100) < 20:
                self.my_quest = Quest(self.date)
        else:  # check for existing quests success
            if self.date == self.my_quest.end_month:
                if self.my_quest.check_quest_overall_success(self.date, self.player):
                    pass  # reward (scoring system)
                else:
                    self.my_quest = None
        """

        self.pay_living_expenses()
        self.pay_loans()
        self.pay_card()

        self.update_salary()
        self.update_credit()
        self.update_assets()
        self.update_netWorth()

        # update community info
        # update crypto info
        # update screen info
        self.update_screen()

    def update_screen(self):
        self.MainWindow.fee_payment_list.clear()
        self.MainWindow.fee_payment_list.addItem("salary: ")
        self.MainWindow.fee_payment_list.addItem(str(self.player.salary))
        self.MainWindow.fee_payment_list.addItem("")
        self.MainWindow.fee_payment_list.addItem("living expenses: ")
        self.MainWindow.fee_payment_list.addItem(str(self.player.livingExpenses))
        self.MainWindow.fee_payment_list.addItem("")
        self.MainWindow.fee_payment_list.addItem("card: ")
        self.MainWindow.fee_payment_list.addItem(str(self.player.card))
        self.MainWindow.fee_payment_list.addItem("")
        self.MainWindow.fee_payment_list.addItem("credit: ")
        self.MainWindow.fee_payment_list.addItem(str(self.player.credit))
        self.MainWindow.fee_payment_list.addItem("")
        self.MainWindow.fee_payment_list.addItem("payments: ")
        self.MainWindow.fee_payment_list.addItem(str(self.player.payments))
        self.MainWindow.fee_payment_list.addItem("")
        self.MainWindow.fee_payment_list.addItem("assets: ")
        for investmentAsset in self.player.assets.investment:
            self.MainWindow.fee_payment_list.addItem(str(investmentAsset.name))
        for propertyAsset in self.player.assets.property:
            self.MainWindow.fee_payment_list.addItem(str(propertyAsset.name))
        self.MainWindow.fee_payment_list.addItem("")
        self.MainWindow.fee_payment_list.addItem("net worth: ")
        self.MainWindow.fee_payment_list.addItem(str(self.player.compute_net_worth()))




