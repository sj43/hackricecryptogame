import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QObject, Signal, Slot

from classes.Player import *
from classes.Community import *


class GameInstance:
    """Game instance """

    max_loan_amount = Signal(float)
    loan_interest = Signal(float)
    see_property = Signal()
    see_investment = Signal()
    pay_living_expenses = Signal(float)
    pay_card = Signal(float)

    def __init__(self, startDate):
        self.date = startDate

        self.player = Player(0, 0, 0, 0, 0, 0)
        self.economy = Economy(0, 0, 0)
        self.bank = Bank()

        self.connect_signals_and_slots()

    def connect_signals_and_slots(self):
        OBJECT.SIGNALNAME.connect(FUNCTIONNAME)

    def player_action(self):
        pass

    @Slot
    def player_ask_loan(self, salary, credit):
        maxLoanAmount = self.bank.howMuchCanILoan(salary, credit)
        loanInterest = self.bank.getLoanInterest(credit)

        self.max_loan_amount.emit(maxLoanAmount)
        self.loan_interest.emit(loanInterest)

    @Slot(float)
    def player_get_loan(self, choicePercent, salary, credit):
        loanAmount = choicePercent * self.bank.howMuchCanILoan(salary, credit)
        loanInterest = self.bank.getLoanInterest(credit)

        self.player.savings += loanAmount
        self.player.payments -= (loanInterest/12.0)*loanAmount

    @Slot
    def player_ask_property(self):
        self.see_property.emit()

    @Slot(int)
    def player_buy_property(self, choiceProperty):
        propertyCost = !!!property.car.cost!!!

        self.player.assets.add_property(!!!property.car.name!!!)
        self.player.savings -= propertyCost

    @Slot
    def player_ask_investment(self):
        self.see_investment.emit()

    @Slot(int)
    def player_make_investment(self, choiceProperty):
        investmentValue = !!!investment.stock.value!!!

        self.player.assets.add_investment(!!!property.stock.name!!!)
        self.player.savings -= investmentValue

    def get_income(self):
        self.player.savings += self.player.salary

        for cryptoAsset in self.player.assets.cryptocurrency:
            !!!self.player.savings += cryptoAsset.income()
        for investmentAsset in self.player.assets.investment:
            self.player.savings += investmentAsset.income()
        for propertyAsset in self.player.assets.property:
            self.player.savings += propertyAsset.income()

    @Slot
    def pay_living_expenses(self):
        self.pay_living_expenses.emit(self.player.livingExpenses)

    @Slot(int)
    def choice_living_expenses(self, choicePayment):
        if choicePayment == 1:
            self.player.card -= self.player.livingExpenses
        elif choicePayment == 2:
            self.player.savings -= self.player.livingExpenses

    def sell_assets(self, paymentLeft):
        for cryptoAsset in self.player.assets.cryptocurrency:
            if paymentLeft <= 0:
                break
            !!!paymentLeft -= !!!cryptoAsset!!!
            !!!self.player.assets.investment.remove(cryptoAsset)
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
        self.player.savings -= paymentLeft
        if self.player.savings < 0:
            self.player.savings = self.sell_assets(-self.player.savings)

    @Slot
    def pay_card(self):
        self.pay_card.emit(5000 - self.player.card)

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

    @Slot
    def end_turn(self):
        # update player info
        self.get_income()

        self.pay_living_expenses()
        self.pay_loans()
        self.pay_card()

        self.player.salary *= 1.0025
        self.player.credit = COMPUTE CREDIT
        self.player.netWorth = self.player.compute_net_worth()

        # update community info
        # update crypto info
        # update screen info
        pass


