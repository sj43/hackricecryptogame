from hackricecryptogame.Crypto.Parsing import *

class Market:
    # The Market is made up of a date represented by a string and a dictionary of Currency prices mapped to Currency names
    def __init__(self, date, collection, monthly_gain):
        self.date = date
        self.collection = collection
        self.monthly = monthly_gain

    def getdate(self):
        return self.date

    def getcollection(self):
        return self.collection

    def getprice(self, cryptoname):
        if cryptoname in self.collection:
            print("The price of " + cryptoname + "is " + self.collection[cryptoname])
        else:
            print(cryptoname + " not found!!")

    def getgrowth(self, cryptoname):
        if cryptoname in self.monthly:
            print("The growth of " + cryptoname + " last month is " + self.monthly[cryptoname])
        else:
            print(cryptoname + " not found!!")

    def update(self, newdate):
        self.date = newdate
        for cryp in finaldict:
            if newdate in finaldict[cryp]:
                self.collection[cryp] = finaldict[cryp][newdate]
            else:
                self.collection[cryp] = -1

    def updatemarket(self, newdate):
        temp = dict()
        for element in self.collection:
            temp[element] = self.collection[element]
        self.update(newdate)
        for name in self.collection:
            if (float(temp[name]) > 0.0):
                self.monthly[name] = str(round((float(self.collection[name]) / float(temp[name]) - 1) * 100, 2)) + "%"
            else:
                self.monthly[name] = None

def datechange(olddate):
    """
    To update the current date by switching to the next month
    :param olddate: the previous date in the format YYYY/MM or YYYY/M
    :return: the new date in the same format
    """
    if (olddate.endswith("12")):
        newyear = int(olddate[0:4]) + 1
        newdate = str(newyear) + "/1"
    elif (olddate[-2] == "/"):
        month = int(olddate[-1]) + 1
        newdate = olddate[:-1] + str(month)
    elif (olddate[-3] == "/"):
        month = int(olddate[-2:]) + 1
        newdate = olddate[:-2] + str(month)
    else:
        newdate = "Formatting Error"
    return newdate

turn = 20
Current = Market("2015/10", {}, {})
Current.update("2015/10")

# A simulation of how the market would react when the game is run
while (turn > 0):
    newdate = datechange(Current.date)
    Current.updatemarket(newdate)
    print(Current.date)
    print(Current.collection)
    print(Current.monthly)
    turn-=1

