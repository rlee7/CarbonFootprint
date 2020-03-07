# returns pounds of Co2 emmissions
# Data from terrapass calcualtor
# 200 miles for work transportation per week
# https://www.nrc.gov/docs/ML1006/ML100621425.pdf
def getMethodOfTransportation(trans):
    if(trans is "electric_car"):
        return 1066
    elif(trans is "bus"):
        return 1216
    elif(trans is "train"):
        return 2658
    elif(trans is "car"):
        return 4000
    elif(trans is "plane"):
        return 2361
    else:
        return 0

# https://www.conservation.org/carbon-footprint-calculator#/individual?zipCodeInfo=usAverage

def getDiet(diet):
    if(diet is "out"):
        return 2000
    elif(diet is "home"):
        return 1500

# https://www.conservation.org/carbon-footprint-calculator#/individual?zipCodeInfo=usAverage
def getMeat(times):
    if(times == 0):
        return 2216
    elif(times < 5 and times > 3 ):
        return 2316
    elif(times > 6):
        return 2450

# https://inhabitat.com/the-pros-and-cons-of-online-versus-in-store-shopping/
def getShopping(shoppingType):
    if(shoppingType is "online"):
        return 2000
    elif(shoppingType is "thrift"):
        return 1000
    elif(shoppingType is "instore"):
        return 1500


# TOTAL SCORE
def getTotal(transType, diet, meatAmount,typeShopping):
    return (getMethodOfTransportation(transType) + getDiet(diet) = getMeat(meatAmount) + getShopping(typeShopping))

