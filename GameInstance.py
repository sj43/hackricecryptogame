import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QObject, Signal, Slot

from GameFunctions import *
from windows.investment_window import *
from windows.property_window import *


class GameInstance(GameFunctions):
    """Game instance """

    def __init__(self, startDate):
        GameFunctions.__init__(startDate)
        self.connect_signals_and_slots()

    def connect_signals_and_slots(self):
        OBJECT.SIGNALNAME.connect(FUNCTIONNAME)

    def player_action(self):
        pass

    @Slot
    def end_turn(self):
        # update player info
        self.get_income()

        self.pay_living_expenses()
        self.pay_loans()
        self.pay_card()

        self.update_salary()
        self.update_credit()
        self.update_assets()
        self.update_netWorth()

        self.date[1] += 1
        if self.date[1] == 13:
            self.date[0] += 1
            self.date[1] = 0

        # update community info
        # update crypto info
        # update screen info
        pass


