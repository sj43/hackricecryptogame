import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QObject, Signal, Slot

from GameFunctions import *
from windows.OptionWindows import *
from classes.quest import *
##from Crypto.market import *


class GameInstance(GameFunctions):
    """Game instance """

    def __init__(self, startDate):
        GameFunctions.__init__(self, startDate)

        MainWindow('main_window.ui')
        PropertyWindow('property_window.ui')
        InvestmentWindow('property_window.ui')
        BankWindow('bank_window.ui')

        self.my_quest = None
        self.connect_signals_and_slots()

    def connect_signals_and_slots(self):
        MainWindow.open_bank.connect(self.player_ask_loan)
        ##MainWindow.open_crypto.connect(CryptoWindow.open_window)
        MainWindow.open_property.connect(self.player_ask_property)
        MainWindow.open_investment.connect(self.player_ask_investment)

        PropertyWindow.buy_property.connect(self.player_buy_property)
        InvestmentWindow.make_investment.connect(self.player_make_investment)
        BankWindow.get_loan.connect(self.player_get_loan)

        self.max_loan_amount.connect(BankWindow.set_loan_amount)
        self.see_loan.connect(BankWindow.open_window)
    
        self.see_property.connect(PropertyWindow.open_window)
        self.see_investment.connect(InvestmentWindow.open_window)

        MainWindow.living_expenses.connect(self.choice_living_expenses)
        MainWindow.card_repay.connect(self.choice_card)
        self.show_payment.connect(MainWindow.display_fee_payment())

    def player_action(self):
        pass
    
    def get_date(self):
        return self.date
    
    @Slot()
    def end_turn(self):
        # update player info
    
        self.get_income()
    
        # show quest here (1. only when there is no existing quest, 2. not always create a quest)
        if self.my_quest == None:
            if random.randint(0, 100) < 20:
                self.my_quest = Quest(self.date)
        else: # check for existing quests success
            if self.date == self.my_quest.end_month:
                if self.my_quest.check_quest_overall_success(self.date, self.player):
                    pass #reward (scoring system)
                else:
                    self.my_quest = None

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
        pass


app = QApplication(sys.argv)
GameInstance('2015/1')
sys.exit(app.exec_())