class Bank:
    """
    Class for bank system.
    """
    def __init__(self, name):
        self.name = name

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

    def howMuchCanILoan(self, player):
        if player.credit >= 720:
            return 3*player.compute_net_worth()
        elif player.credit >= 680:
            return 2*player.compute_net_worth()
        elif player.credit >= 640:
            return player.compute_net_worth()
        else:
            return -1

    def getLoanInterest(self, player):
        """
        FICO credit score ranges from 300 to 850.
        less than 660 is poor, over 660 is good, and 800 is excellent.
        """
        if player.credit >= 720:
            return 0.11
        elif player.credit >= 680:
            return 0.14
        elif player.credit >= 640:
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
