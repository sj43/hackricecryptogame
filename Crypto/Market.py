import csv
from Crypto.Parse import finaldict

dataset = p.finaldict()
class Market:
    # The Market is made up of a date and a dictionary of Currency prices mapped to Currency names
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
        for cryp in finaldict():
            if newdate in finaldict[cryp]:
                self.collection[cryp] = finaldict[cryp][newdate]
            else:
                self.collection[cryp] = -1

    def original(self, newdate):
        self.collection = {}
        self.update(newdate)

Current = Market("2015/10/1", {})
Current.update("2015/11/1")
print(Current.collection)
print(Current.date)
