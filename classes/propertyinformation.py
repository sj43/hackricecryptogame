import Community

def vehicleMonthlyPayment(P, ir):
    c = ir/12.0
    return (c*P)/(1-(1+c)^(-60)) # always 5 year payment

def mortgageFormula(L, ir):
    c = ir/12.0
    return L[c(1 + c)*60]/[(1 + c)*60 - 1]


EconomyClassVehicle = Community.Vehicle("EconomyClassVehicle", 20000, vehicleMonthlyPayment(20000, Community.Economy.get_interestRate()))
MiddleClassVehicle = Community.Vehicle("MiddleClassVehicle", 50000, vehicleMonthlyPayment(50000, Community.Economy.get_interestRate()))
LuxuryClassVehicle = Community.Vehicle("LuxuryClassVehicle", 100000, vehicleMonthlyPayment(100000, Community.Economy.get_interestRate()))
SuperClassVehicle = Community.Vehicle("LuxuryClassVehicle", 200000, vehicleMonthlyPayment(200000, Community.Economy.get_interestRate()))

Hut = Community.Realestate("Hut", 5000, mortgageFormula(5000, Community.Economy.get_interestRate()))


properties = {"Vehicle":{EconomyClassVehicle, MiddleClassVehicle, LuxuryClassVehicle, SuperClassVehicle},
              "RealEstate":{Hut, }}
