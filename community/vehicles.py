class Vehicle:
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
        if self.value == self.paid:
            return True
        else:
            False
