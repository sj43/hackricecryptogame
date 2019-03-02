import economy
import accountinformation


class bank:
    """
    Class for bank system.
    """
    def __init__(self, player):
        self.interest_rate =
        self.bank_capital = economy.total_money_in_economy
        self.account = accountinformation.accountinfo

    def menu(self):
        print("Welcome to Bank!")
        print("What would you like to do?")
        print("")
        print("1. Deposit $$")
        print("2. Withdraw $$")
        print("3. Loan $$")
        print("4. Check Current Balance")
        print("5. Check Credit")
        print("6. Leave Bank")
        print("")
        user_input = input()
        if user_input == 1:
            print("How much?")
            m = input()
            deposit(m)
        if user_input == 2:
            print("How much?")
            m = input()
            withdraw(m)
        if user_input == 3:
            print("How much?")
            m = input()
            withdraw(m)
        if user_input == 4:
            print("Your balance is: ", printBalance())
        if user_input == 5:
            print("Your credit is: ", checkCredit())
        if user_input == 6:
            print("Thank you!")

    def deposit(self, amount):
        self.account["savings"] += amount
        player.savings -= amount

    def withdraw(self. amount):
        if self.account["savings"] >= amount:
            self.account["savings"] -= amount
            player.savings += amount
        else:
            print("Not enough money :(")

    def loan(self, amount):
        """
        FICO credit score ranges from 300 to 850.
        less than 660 is poor, over 660 is good, and 800 is excellent.
        """
        if self.account["credit"] > 720:
            self.interest_rate = 0.11
            total_money_in_economy -= amount
            player.debt += amount
            player.savings += amount
        else if self.account["credit"] > 680:
            self.interest_rate = 0.14
            total_money_in_economy -= amount
            player.debt += amount
            player.savings += amount
        else if self.account["credit"] > 640:
            self.interest_rate = 0.18
            total_money_in_economy -= amount
            player.debt += amount
            player.savings += amount
        else:
            print("Your credit is too low for any loan...")

    def printBalance(self):
        return self.account["savings"]

    def checkCredit(self):
        return self.account["credit"]

    def calculateNewDebt(self):
        """
        Needs to be called every month!
        """
        ir = self.account["interest_rate"]
        ir /= 12.0
        self.account["debt"] = self.account["debt"] * (1 + ir)




B = bank()
