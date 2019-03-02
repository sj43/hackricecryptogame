import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QObject, Signal, Slot

from hackricecryptogame.GameFunctions import *
from windows.OptionWindows import *
from classes.quest import *
from Crypto.market import *

class GameInstance(GameFunctions):
    """Game instance """

    def __init__(self, startDate):
        GameFunctions.__init__(self, startDate)

        PropertyWindow('property_window.ui')
        InvestmentWindow('property_window.ui')

        self.connect_signals_and_slots()

        self.my_quest = None

    def connect_signals_and_slots(self):
        PropertyWindow.buy_property.connect(self.player_buy_property)
        InvestmentWindow.make_investment.connect(self.player_make_investment)

    def player_action(self):
        pass

    def get_date(self):
        return self.date

    @Slot
    def end_turn(self):
        # update player info

        self.get_income()

        # show quest here (1. only when there is no existing quest, 2. not always create a quest)
        if self.my_quest == None:
            if random.randint(0, 100) < 20:
                self.my_quest = Quest()
        else: # check for existing quests success
            if self.my_quest.check_quest_overall_success(self.date, self.player):
                pass #reward
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
