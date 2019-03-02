import csv

crypto_to_data = {"Bitcoin": "btc",
                  "Dash": "dash",
                  "Ethereum": "eth",
                  "Litecoin": "ltc",
                  "Tether": "usdt",
                  "Stellar": "xlm",
                  "Ripple": "xrp"}

def read(cryptoname):
    """
    Given a name of one of the 7 cryptocurrency, return a dictionary corresponding to it,
    with dates as keys and price for that date as the values.
    """

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
    # Create our dataset for the price of each cryptocurrency at the first day of any given month
    finaldict[item] = read(item)




