from resources.Parsing import *

class Market:
    # The Market is made up of a set of Currencies
    def __init__(self, date, collection):
        self.date = date
        self.collection = collection

    def getdate(self):
        return self.date

    def getcollection(self):
        return self.collection

    def getprice(self, cryptoname):
        if cryptoname in self.collection:
            print("The price of " + cryptoname + "is " + self.collection[cryptoname])
        else:
            print(cryptoname + " not found!!")

    def update(self, newdate):
        self.date = newdate
        for cryp in finaldict:
            if date in finaldict[cryp]:
                self.collection[cryp] = finaldict[cryp][date]
            else:
                self.collection[cryp] = -1

    def original(self, newdate):
        self.collection = {}
        self.update(newdate)

