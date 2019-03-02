import csv

crypto_to_data = {"Bitcoin": "btc",
                  "Dash": "dash",
                  "Ethereum": "eth",
                  "Litecoin": "ltc",
                  "Tether": "usdt",
                  "Stellar": "xlm",
                  "Ripple": "xrp"}

def read(cryptoname):
    dict = {}
    abbre = crypto_to_data[cryptoname]
    str = abbre + ".csv"
    with open(str, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['date'].endswith("/1"):
                dict[row['date']] = row['price(USD)']
    return dict

finaldict = {}
for item in crypto_to_data:
    finaldict[item] = read(item)

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

    def original(self, newdate):
        self.collection = {}
        self.update(newdate)

Current = Market("2015/10/1", {})
Current.update("2015/11/1")
print(Current.collection)
print(Current.date)
