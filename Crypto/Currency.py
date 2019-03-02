class Currency:
    # Each Currency has a name and a price
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __getname__(self):
        return self.name

    def __getprice__(self):
        return self.price

    def update(self, newprice):
        self.price = newprice

class Market:
    # The Market is made up of a set of Currencies
    def __init__(self, collection):
        self.collection = collection

    def add(self, cryptoobj):
        self.collection.add(cryptoobj)

    def drop(self, crypto):
        for cryp in self.collection:
            if cryp.name == crypto:
                self.collection.remove(cryp)

    def empty(self):
        return Market(set())

def allcrypto():
    collection = set()

crypto_to_abbreviation = {"Cardano":"ada","bitcoin":"bch",
                          }
