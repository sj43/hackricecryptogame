from hackricecryptogame.Crypto.Parsing import *

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
        for cryp in finaldict:
            if newdate in finaldict[cryp]:
                self.collection[cryp] = finaldict[cryp][newdate]
            else:
                self.collection[cryp] = -1

Current = Market("2015/10/1", {})
Current.update("2015/10/1")
print(Current.collection)
print(Current.date)

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

print(datechange("2014/1"))
print(datechange("2014/12"))
print(datechange("2016/4"))
print(datechange("2018/10"))

