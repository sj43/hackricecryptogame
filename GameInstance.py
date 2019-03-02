import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QObject, Signal, Slot

from GameFunctions import *
from windows.OptionWindows import *
from classes.quest import *


class GameInstance(GameFunctions):
    """Game instance """

    def __init__(self, startDate):
        GameFunctions.__init__(self, startDate)

        PropertyWindow('property_window.ui')
        InvestmentWindow('property_window.ui')

        self.connect_signals_and_slots()

    def connect_signals_and_slots(self):
        PropertyWindow.buy_property.connect(self.player_buy_property)
        InvestmentWindow.make_investment.connect(self.player_make_investment)
        BankWindow.get_loan.connect(self.player_get_loan)

        self.see_loan.connect(BankWindow.open_window)
        self.max_loan_amount.connect(BankWindow.set_loan_amount)

        self.see_property.connect(PropertyWindow.open_window)
        self.see_investment.connect(InvestmentWindow.open_window)

        //pay_living_expenses = Signal(float)
        //pay_card = Signal(float)

    def player_action(self):
        pass
    
    def get_date(self):
        return self.date
    
    @Slot
    def end_turn(self):
        # update player info
    
        self.get_income()
    
        # show quest here
        new_quest = Quest()
    
        # check for existing quests success
        self.is_quest_done()


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
