import sys
import random
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QObject, Signal, Slot

class Economy:
    """Class for economy and market conditions"""

    def __init__(self, interestRate, growthGDP, stockIndex):
        self.interestRate = interestRate
        self.growthGDP = growthGDP
        self.stockIndex = stockIndex

    def set_interestRate(self, newAmount):
        self.interestRate = newAmount

    def set_growthGDP(self, newAmount):
        self.growthGDP = newAmount

    def set_stockIndex(self, newAmount):
        self.stockIndex = changeAmount

    def get_interestRate(self):
        return self.interestRate


class Bank:
    """Class for bank system"""

    def updateCreditScore(self, player):
        if player.creditcard < 1000:
            amount_to_change = -300
        elif player.creditcard < 3000:
            amount_to_change = -100
        elif player.creditcard < 4500:
            amount_to_change = -50
        elif player.creditcard < 5000:
            amount_to_change = -20
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

    def calculateNewDebt(self, player):
        """
        Needs to be called every month!
        """
        ir = player.interest_rate
        ir /= 12.0
        return player.debt * (1 + ir)


class Realestate:
    """Class for realestate system"""

    def __init__(self, name, value, rent):
        self.name = name
        self.value = value
        self.rent = rent
        self.owner = ""
        self.paid = 0.0

    def info(self):
        print(self.name, self.value, self.rent, self.owner)

    def buyIt(self, amount_paid):
        self.owner = "YOU"
        self.paid += amount_paid

    def howMuchLeftToPayOff(self):
        return self.value - self.paid

    def isPaidOff(self):
        return self.value == self.paid


class Vehicle:
    """Class for vehicle system"""

    def __init__(self, name, value, fee):
        self.name = name
        self.value = value
        self.fee = fee
        self.owner = ""
        self.paid = 0.0

    def info(self):
        print(self.name, self.value, self.fee, self.owner)

    def buyIt(self, amount_paid):
        self.owner = "YOU"
        self.paid += amount_paid

    def howMuchLeftToPayOff(self):
        return self.value - self.paid

    def isPaidOff(self):
        return self.value == self.paid


class Stock:
    """
    Class for stock system
    Notice that "kind" is one of "low", "avg", or "high"
    """

    def __init__(self, initial_amount, kind): # kind = one of "low", "avg", or "high"
        self.initial_amount = initial_amount
        self.kind = kind

    def generate_random_return_percentage(self, a, b):
        return random.uniform(a, b)

    def generate_return(self, whatkind):
        if whatkind == "low":
            return generate_random_return_percentage(-0.05, 0.05)
        elif whatkind == "avg":
            return generate_random_return_percentage(-0.15, 0.15)
        elif whatkind == "high":
            return generate_random_return_percentage(-0.3, 0.3)
        else: # error
            return -1

    def return_result(self):
        return self.initial_amount * (1 + generate_return(self.kind))


class FixedSaving:
    """Class for fixed saving system"""

    def __init__(self, initial_amount, year, rate):
        self.return_amount = initial_amount * (1 + rate/4.0/100) ^ (4 * year)

    def return_result(self):
        return self.return_amount
