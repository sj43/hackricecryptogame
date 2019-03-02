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
        for investmentAsset in self.player.assets.investment:
            paymentLeft -= investmentAsset.investmentValue
            if paymentLeft <= 0:
                break
        for investmentAsset in self.player.assets.investment:
            paymentLeft -= investmentAsset.investmentValue
            self.player.assets.investment.remove(investmentAsset)
            if paymentLeft <= 0:
                break
        for propertyAsset in self.player.assets.property:
            paymentLeft -= propertyAsset.propertyValue
            self.player.assets.investment.remove(propertyAsset)
            if paymentLeft <= 0:
                break

    def pay_loans(self):
        paymentLeft = self.player.payments
        if self.player.savings >= paymentLeft:
            self.player.savings -= paymentLeft
        else:
            paymentLeft -= self.player.savings
            self.player.savings = 0

            self.player.savings = -paymentLeft

    @Slot
    def pay_card(self):
        self.pay_card.emit(5000 - self.player.card)

    @Slot(int)
    def choice_card(self, choiceCard):
        if choiceCard == 1:
            if self.player.savings >= self.player.card:
                self.player.savings -= self.player.card
                self.player.card = 0
            else:
                self.player.card -= self.player.savings
                self.player.savings = 0
        elif choiceCard == 2:
            self.player.savings -= self.player.livingExpenses

    def end_turn(self):
        # update player info
        self.pay_living_expenses()
        self.pay_loans()
        self.pay_card()
        # update community info
        # update crypto info
        # update screen info
        pass


