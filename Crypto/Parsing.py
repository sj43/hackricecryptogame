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
                dict[row['date']] = [row['price(USD)'], ]
    return dict


finaldict = {}
for item in crypto_to_data:
    finaldict[item] = read(item)

def datechange(olddate):
    if olddate.endswith()
    newdate =


