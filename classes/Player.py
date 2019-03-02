import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QObject, Signal, Slot

import random

from classes.Community import *
from classes.Information import *

class Property:
    """Class for large assets (real estate, vehicles)"""

    def __init__(self, name, propertyValue):
        self.name = name
        self.propertyValue = propertyValue

    def income(self):
        if "estate" in self.name:
            return self.propertyValue * 0.01
        if "vehicle" in self.name:
            return self.propertyValue * 0.02

class Investment:
    """Class for financial investments (stocks, fixed savings)"""

    def __init__(self, name, investmentValue, fixedCount=0):
        self.name = name
        self.investmentValue = investmentValue
        if "3" in self.name:
            self.fixedCount = 3
        if "6" in self.name:
            self.fixedCount = 6
        if "12" in self.name:
            self.fixedCount = 12
        self.fixedInterest = 0.002

    def income(self):
        if "stock" in self.name:
            if "low" in self.name:
                return self.investmentValue * random.uniform(-0.002, 0.004)
            if "avg" in self.name:
                return self.investmentValue * random.uniform(-0.004, 0.008)
            if "high" in self.name:
                return self.investmentValue * random.uniform(-0.008, 0.016)
        if "fixed" in self.name:
            self.fixedCount -= 1
            self.fixedInterest += 0.0001
            if self.fixedCount == 0:
                return self.investmentValue * (1 + self.fixedInterest)
            else:
                return -1

class CryptoCurrency:
    """Class for cryptocurrency"""

    def __init__(self, name, currencyValue):
        self.name = name
        self.currencyValue = currencyValue


class PlayerAssets:
    """Class for player assets"""

    def __init__(self):
        self.property = []
        self.investment = []
        self.cryptocurrency = []

    def add_property(self, propertyInfo):
        self.property.append(Property(propertyInfo[0], propertyInfo[1]))

    def add_investment(self, investmentInfo):
        self.property.append(Investment(investmentInfo[0], investmentInfo[1]))

    def add_cryptocurrency(self, cryptoAsset):
        self.property.append(cryptoAsset)


class Player:
    """Class for game player finances"""

    def __init__(self, salary, livingExpenses, savings, card, credit, payments):
        self.salary = salary
        self.livingExpenses = livingExpenses
        self.savings = savings
        self.card = card
        self.credit = credit
        self.payments = payments
        self.assets = PlayerAssets()
        self.netWorth = self.compute_net_worth()

    def compute_net_worth(self):
        netWorth = self.savings

        for property in self.assets.property:
            netWorth += property.propertyValue
        for investment in self.assets.investment:
            netWorth += investment.investmentValue
        for cryptocurrency in self.assets.cryptocurrency:
            netWorth += cryptocurrency.currencyValue

        return netWorth

