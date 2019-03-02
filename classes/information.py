def get_property(choiceProperty):
    return property_choices[choiceProperty + 1]


def get_investment(choiceInvestment):
    return property_choices[choiceInvestment + 1]


# Choices
property_choices = (("vehicle_economy", 20000),
                    ("vehicle_middle", 50000),
                    ("vehicle_luxury", 100000),
                    ("estate_apartment", 150000),
                    ("estate_house", 300000),
                    ("estate_penthouse", 600000))
investment_choices = (("stock_low", 1000),
                      ("stock_avg", 1000),
                      ("stock_high", 1000),
                      ("fixed_3", 1000),
                      ("fixed_6", 1000),
                      ("fixed_12", 1000))


"""
# Vehicle
Bicycle = Community.Vehicle("Bicycle", 300, vehicleMonthlyPayment(300, Community.Economy.get_interestRate()))
EconomyClassVehicle = Community.Vehicle("EconomyClassVehicle", 20000, vehicleMonthlyPayment(20000, Community.Economy.get_interestRate()))
MiddleClassVehicle = Community.Vehicle("MiddleClassVehicle", 50000, vehicleMonthlyPayment(50000, Community.Economy.get_interestRate()))
LuxuryClassVehicle = Community.Vehicle("LuxuryClassVehicle", 100000, vehicleMonthlyPayment(100000, Community.Economy.get_interestRate()))
SuperClassVehicle = Community.Vehicle("SuperClassVehicle", 200000, vehicleMonthlyPayment(200000, Community.Economy.get_interestRate()))

# RealEstate
Hut = Community.Realestate("Hut", 5000, mortgageFormula(5000, Community.Economy.get_interestRate()))
Garage = Community.Realestate("Garage", 30000, mortgageFormula(30000, Community.Economy.get_interestRate()))
OneBedroomApt = Community.Realestate("OneBedroomApt", 100000, mortgageFormula(100000, Community.Economy.get_interestRate()))
TwoBedroomApt = Community.Realestate("TwoBedroomApt", 170000, mortgageFormula(170000, Community.Economy.get_interestRate()))
House = Community.Realestate("House", 300000, mortgageFormula(300000, Community.Economy.get_interestRate()))
Penthouse = Community.Realestate("Penthouse", 500000, mortgageFormula(500000, Community.Economy.get_interestRate()))
Mansion = Community.Realestate("Penthouse", 1000000, mortgageFormula(1000000, Community.Economy.get_interestRate()))

#stocks -- NEED TO CALL the method "return_result" !
low_risk_low_return_50000 = Community.Stock(50000, "low")
avg_risk_avg_return_50000 = Community.Stock(50000, "avg")
high_risk_high_return_50000 = Community.Stock(50000, "high")

low_risk_low_return_100000 = Community.Stock(100000, "low")
avg_risk_avg_return_100000 = Community.Stock(100000, "avg")
high_risk_high_return_100000 = Community.Stock(100000, "high")

low_risk_low_return_500000 = Community.Stock(500000, "low")
avg_risk_avg_return_500000 = Community.Stock(500000, "avg")
high_risk_high_return_500000 = Community.Stock(500000, "high")

low_risk_low_return_1000000 = Community.Stock(1000000, "low")
avg_risk_avg_return_1000000 = Community.Stock(1000000, "avg")
high_risk_high_return_1000000 = Community.Stock(1000000, "high")

# Fixed Saving -- Whatkind_initialamount_years
fixed_50000_2 = Community.FixedSaving(50000, 2, 0.005)
fixed_50000_5 = Community.FixedSaving(50000, 5, 0.007)
fixed_50000_10 = Community.FixedSaving(50000, 10, 0.01)

fixed_100000_2 = Community.FixedSaving(100000, 2, 0.005)
fixed_100000_5 = Community.FixedSaving(100000, 5, 0.007)
fixed_100000_10 = Community.FixedSaving(100000, 10, 0.01)

fixed_500000_2 = Community.FixedSaving(500000, 2, 0.005)
fixed_500000_5 = Community.FixedSaving(500000, 5, 0.007)
fixed_500000_10 = Community.FixedSaving(500000, 10, 0.01)

fixed_1000000_2 = Community.FixedSaving(1000000, 2, 0.005)
fixed_1000000_5 = Community.FixedSaving(1000000, 5, 0.007)
fixed_1000000_10 = Community.FixedSaving(1000000, 10, 0.01)

# Choices
property_choices = {"Vehicle":{Bicycle, EconomyClassVehicle, MiddleClassVehicle, LuxuryClassVehicle, SuperClassVehicle},
                   "RealEstate":{Hut, Garage, OneBedroomApt, TwoBedroomApt, House, Penthouse, Mansion}}

stock_choices = {low_risk_low_return_50000,
                avg_risk_avg_return_50000,
                high_risk_high_return_50000,
                low_risk_low_return_100000,
                avg_risk_avg_return_100000,
                high_risk_high_return_100000,
                low_risk_low_return_500000,
                avg_risk_avg_return_500000,
                high_risk_high_return_500000,
                low_risk_low_return_1000000,
                avg_risk_avg_return_1000000,
                high_risk_high_return_1000000}

fixedsaving_choices = {fixed_50000_2,
                      fixed_50000_5,
                      fixed_50000_10,
                      fixed_100000_2,
                      fixed_100000_5,
                      fixed_100000_10,
                      fixed_500000_2,
                      fixed_500000_5,
                      fixed_500000_10,
                      fixed_1000000_2,
                      fixed_1000000_5,
                      fixed_1000000_10}
"""
