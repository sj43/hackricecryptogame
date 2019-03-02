import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QObject, Signal, Slot

from GameFunctions import *
from classes.quest import *

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
        quest = Quest()


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
