import Community

def vehicleMonthlyPayment(P, ir):
    c = ir/12.0
    return (c*P)/(1-(1+c)^(-60)) # always 5 year payment

def mortgageFormula(L, ir):
    c = ir/12.0
    return L[c(1 + c)*60]/[(1 + c)*60 - 1]

# Vahicle
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



properties = {"Vehicle":{Bicycle, EconomyClassVehicle, MiddleClassVehicle, LuxuryClassVehicle, SuperClassVehicle},
              "RealEstate":{Hut, Garage, OneBedroomApt, TwoBedroomApt, House, Penthouse, Mansion}}
