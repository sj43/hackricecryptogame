from windows.OptionWindows import *
from GameFunctions import *
# from classes.quest import *
# from Crypto.market import *


class GameInstance(GameFunctions):
    """Game instance """

    def __init__(self, startDate):
        GameFunctions.__init__(self, startDate)

        app = QApplication(sys.argv)
        self.main_window = MainWindow("windows/main_window.ui")
        self.crypto_window = CryptoWindow('windows/crypto_window.ui')
        self.property_window = PropertyWindow('windows/property_window.ui')
        self.investment_window = InvestmentWindow('windows/investment_window.ui')
        self.bank_window = BankWindow('windows/bank_window.ui')
        self.connect_signals_and_slots()
        sys.exit(app.exec_())

    def connect_signals_and_slots(self):
        self.main_window.open_crypto.connect(self.crypto_window.open_window)
        self.main_window.open_property.connect(self.player_ask_property)
        self.main_window.open_investment.connect(self.player_ask_investment)
        self.main_window.open_bank.connect(self.player_ask_loan)

        self.crypto_window.buy_crypto.connect(self.player_buy_crypto)
        self.crypto_window.sell_crypto.connect(self.player_sell_crypto)
        self.property_window.buy_property.connect(self.player_buy_property)
        self.investment_window.make_investment.connect(self.player_make_investment)
        self.bank_window.get_loan.connect(self.player_get_loan)

        self.max_loan_amount.connect(self.bank_window.set_loan_amount)
        self.see_loan.connect(self.bank_window.open_window)

        self.see_property.connect(self.property_window.open_window)
        self.see_investment.connect(self.investment_window.open_window)

        self.main_window.living_expenses.connect(self.choice_living_expenses)
        self.main_window.card_repay.connect(self.choice_card)
        # self.show_payment.connect(self.main_window.display_fee_payment())

        self.main_window.end_turn_signal.connect(self.end_turn)

    def player_action(self):
        pass

    def get_date(self):
        return self.date

    @Slot()
    def end_turn(self):
        # update player info

        self.get_income()

        # show quest here (1. only when there is no existing quest, 2. not always create a quest)
        """
        if self.my_quest == None:
            if random.randint(0, 100) < 20:
                self.my_quest = Quest(self.date)
        else:  # check for existing quests success
            if self.date == self.my_quest.end_month:
                if self.my_quest.check_quest_overall_success(self.date, self.player):
                    pass  # reward (scoring system)
                else:
                    self.my_quest = None
        """

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
        self.update_screen()

    def update_screen(self):
        self.main_window.fee_payment_list.clear()
        self.main_window.fee_payment_list.addItem("salary: ")
        self.main_window.fee_payment_list.addItem(str(self.player.salary))
        self.main_window.fee_payment_list.addItem("")
        self.main_window.fee_payment_list.addItem("living expenses: ")
        self.main_window.fee_payment_list.addItem(str(self.player.livingExpenses))
        self.main_window.fee_payment_list.addItem("")
        self.main_window.fee_payment_list.addItem("savings: ")
        self.main_window.fee_payment_list.addItem(str(self.player.savings))
        self.main_window.fee_payment_list.addItem("")
        self.main_window.fee_payment_list.addItem("card: ")
        self.main_window.fee_payment_list.addItem(str(self.player.card))
        self.main_window.fee_payment_list.addItem("")
        self.main_window.fee_payment_list.addItem("credit: ")
        self.main_window.fee_payment_list.addItem(str(self.player.credit))
        self.main_window.fee_payment_list.addItem("")
        self.main_window.fee_payment_list.addItem("payments: ")
        self.main_window.fee_payment_list.addItem(str(self.player.payments))
        self.main_window.fee_payment_list.addItem("")
        self.main_window.fee_payment_list.addItem("assets: ")
        for investmentAsset in self.player.assets.investment:
            self.main_window.fee_payment_list.addItem(str(investmentAsset.name))
        for propertyAsset in self.player.assets.property:
            self.main_window.fee_payment_list.addItem(str(propertyAsset.name))
        self.main_window.fee_payment_list.addItem("")
        self.main_window.fee_payment_list.addItem("net worth: ")
        self.main_window.fee_payment_list.addItem(str(self.player.compute_net_worth()))

