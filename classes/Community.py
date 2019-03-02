import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QObject, Signal, Slot

import random

class Economy:
    """Class for economy and market conditions"""

    def __init__(self, interestRate, growthGDP):
        self.interestRate = interestRate
        self.growthGDP = growthGDP

    def set_interestRate(self, newAmount):
        self.interestRate = newAmount

    def set_growthGDP(self, newAmount):
        self.growthGDP = newAmount


class Bank:
    """Class for bank system"""

    def updateCreditScore(self, card):
        if card < 1000:
            amount_to_change = -100
        elif card < 3000:
            amount_to_change = -50
        elif card < 4500:
            amount_to_change = -20
        elif card < 5000:
            amount_to_change = 0
        else:
            amount_to_change = 20
        return amount_to_change

    def howMuchCanILoan(self, salary, credit):
        if credit >= 720:
            return 3*salary
        elif credit >= 680:
            return 2*salary
        elif credit >= 640:
            return 1*salary
        else:
            return -1

    def getLoanInterest(self, credit):
        """
        FICO credit score ranges from 300 to 850.
        less than 660 is poor, over 660 is good, and 800 is excellent.
        """
        if credit >= 720:
            return 0.11
        elif credit >= 680:
            return 0.14
        elif credit >= 640:
            return 0.19
        else:
            return -1
