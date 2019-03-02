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

    def __init__(self, startDate):
        self.date = startDate

        self.player = PlayerClass(0, 0, 0, 0, 0, 0)
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
        property

    def end_turn(self):
        # update player info
        # update community info
        # update crypto info
        pass


