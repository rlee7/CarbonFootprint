# returns kg of co2 emission
def getMethodOfTransportation(trans):
    if(trans is "electric_car"):
        return 11
    elif(trans is "bus"):
        return 24
    elif(trans is "train"):
        return 84.3
    elif(trans is "car"):
        return 80.7
    elif(trans is "plane"):
        return 75.3
    else:
        return 0


def getDiet(diet):
    if(diet is "out"):
        return 30
    elif(diet is "home"):
        return 10

def getMeat(times):
    return 40 * times

def getShopping(times):
    return 50 * times


