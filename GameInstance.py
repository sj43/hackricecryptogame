import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QObject, Signal, Slot

from GameFunctions import *
from windows.investment_window import *
from windows.property_window import *
from classes.quest import *
from Crypto.market import *


class GameInstance(GameFunctions):
    """Game instance """

    def __init__(self, startDate):
        GameFunctions.__init__(startDate)
        self.connect_signals_and_slots()
    
    def connect_signals_and_slots(self):
        OBJECT.SIGNALNAME.connect(FUNCTIONNAME)
    
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
