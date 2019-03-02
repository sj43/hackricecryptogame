class Property:
    """Class for large assets (real estate, vehicles, jewelery)"""

    def __init__(self, name, propertyValue, payment, income):
        self.name = name
        self.propertyValue = propertyValue
        self.payment = payment
        self.income = income

    def change_value(self, changeAmount):
        self.propertyValue += changeAmount

    def change_payment(self, changeAmount):
        self.payment += changeAmount

    def change_income(self, changeAmount):
        self.income += changeAmount


class Investment:
    """Class for financial investments (stocks, fixed savings, insurance)"""

    def __init__(self, name, investmentValue, payment, income):
        self.name = name
        self.investmentValue = investmentValue
        self.payment = payment
        self.income = income

    def change_value(self, changeAmount):
        self.investmentValue += changeAmount

    def change_payment(self, changeAmount):
        self.payment += changeAmount

    def change_income(self, changeAmount):
        self.income += changeAmount


class CryptoCurrency:
    """Class for cryptocurrency"""

    def __init__(self, name, currencyValue):
        self.name = name
        self.currencyValue = currencyValue

    def change_value(self, changeAmount):
        self.currencyValue += changeAmount


class PlayerAssets:
    """Class for player assets"""

    def __init__(self):
        self.property = []
        self.investment = []
        self.cryptocurrency = []

    def change_savings(self, changeAmount):
        self.savings += changeAmount

    def add_property(self, property):
        self.property.append(property)

    def add_investment(self, investment):
        self.property.append(investment)

    def add_cryptocurrency(self, cryptocurrency):
        self.property.append(cryptocurrency)


class PlayerFinances:
    """Class for game player finances"""

    def __init__(self, salary, livingExpenses, savings, credit, debt):
        self.salary = salary
        self.livingExpenses = livingExpenses
        self.savings = savings
        self.credit = credit
        self.debt = debt
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

