import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QObject, Signal, Slot

from classes.Player import *
from classes.Community import *
from classes.Information import *
##from Crypto.Parse import *
##from Crypto.Market import *


class GameFunctions(QObject):
    """Game functions"""

    max_loan_amount = Signal(float, float)
    see_loan = Signal()
    see_property = Signal()
    see_investment = Signal()
    show_payment = Signal(float)

    def __init__(self, startDate, parent=None):
        super(GameFunctions, self).__init__(parent)
        self.date = startDate

        self.player = Player(100000, 500, 100000, 5000, 700, 0)
        self.economy = Economy(0.05, 5.0)
        self.bank = Bank()

    @Slot()
    def player_ask_loan(self):
        maxLoanAmount = self.bank.howMuchCanILoan(self.player.salary, self.player.credit)
        loanInterest = self.bank.getLoanInterest(self.player.credit)

        self.max_loan_amount.emit(maxLoanAmount, loanInterest)
        self.see_loan.emit()

    @Slot(float)
    def player_get_loan(self, choicePercent):
        loanAmount = choicePercent * self.bank.howMuchCanILoan(self.player.salary, self.player.credit)
        loanInterest = self.bank.getLoanInterest(self.player.credit)

        self.player.savings += loanAmount
        self.player.payments -= (loanInterest/12.0)*loanAmount

    @Slot()
    def player_ask_property(self):
        self.see_property.emit()

    @Slot(int)
    def player_buy_property(self, choiceProperty):
        propertyInfo = get_property(choiceProperty)

        self.player.assets.add_property(propertyInfo)
        self.player.savings -= propertyInfo[1]

    @Slot()
    def player_ask_investment(self):
        self.see_investment.emit()

    @Slot(int)
    def player_make_investment(self, choiceInvestment):
        investmentInfo = get_investment(choiceInvestment)

        self.player.assets.add_investment(investmentInfo)
        self.player.savings -= investmentInfo[1]

    def get_income(self):
        self.player.savings += self.player.salary

        ##for cryptoAsset in self.player.assets.cryptocurrency:
        ##    self.player.savings += cryptoAsset.income()
        for investmentAsset in self.player.assets.investment:
            self.player.savings += investmentAsset.income()
        for propertyAsset in self.player.assets.property:
            self.player.savings += propertyAsset.income()

    def pay_living_expenses(self):
        self.show_payment.emit(self.player.livingExpenses)

    @Slot(int)
    def choice_living_expenses(self, choicePayment):
        if choicePayment == 1:
            self.player.card -= self.player.livingExpenses
        elif choicePayment == 2:
            self.player.savings -= self.player.livingExpenses

    def sell_assets(self, paymentLeft):
        ##for cryptoAsset in self.player.assets.cryptocurrency:
        ##    if paymentLeft <= 0:
        ##        break
        ##    paymentLeft -= cryptoAsset
        ##    self.player.assets.investment.remove(cryptoAsset)
        for investmentAsset in self.player.assets.investment:
            if paymentLeft <= 0:
                break
            paymentLeft -= investmentAsset.investmentValue
            self.player.assets.investment.remove(investmentAsset)
        for propertyAsset in self.player.assets.property:
            if paymentLeft <= 0:
                break
            paymentLeft -= propertyAsset.propertyValue
            self.player.assets.investment.remove(propertyAsset)

        return -paymentLeft

    def pay_loans(self):
        paymentLeft = self.player.payments
        self.show_payment.emit(paymentLeft)

        self.player.savings -= paymentLeft
        if self.player.savings < 0:
            self.player.savings = self.sell_assets(-self.player.savings)

    def pay_card(self):
        self.show_payment.emit(5000 - self.player.card)

    @Slot(int)
    def choice_card(self, choiceCard):
        paymentLeft = 5000 - self.player.card
        if choiceCard == 1:
            self.player.savings -= paymentLeft
            if self.player.savings < 0:
                self.player.savings = self.sell_assets(-self.player.savings)
            self.player.card = 0
        elif choiceCard == 2:
            self.player.savings -= paymentLeft * 0.015
            if self.player.savings < 0:
                self.player.savings = self.sell_assets(-self.player.savings)

    def update_salary(self):
        self.player.salary *= 1.0025

    def update_credit(self):
        self.player.credit += self.bank.updateCreditScore(self.player.card)
        if self.player.credit < 300:
            self.player.credit = 300
        if self.player.credit > 850:
            self.player.credit = 850

    def update_assets(self):
        for investmentAsset in self.player.assets.investment:
            if "stock" in investmentAsset.name:
                growth = 1.0 + (random.gauss(self.economy.growthGDP, 5) / 100)
                if (growth < -0.5) or (growth > 0.5):
                    growth = 1.0
                investmentAsset.investmentValue *= growth
            if "fixed" in investmentAsset.name:
                if investmentAsset.fixedCount == 0:
                    self.player.assets.investment.remove(investmentAsset)
        for propertyAsset in self.player.assets.property:
            if "estate" in propertyAsset.name:
                propertyAsset.propertyValue *= (1 + self.economy.interestRate/12.0)
            if "vehicle" in propertyAsset.name:
                propertyAsset.propertyValue *= 0.98

    def update_netWorth(self):
        self.player.netWorth = self.player.compute_net_worth()

