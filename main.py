import random
import math

def randomCityGenerator():             # creates 5 random (x,y) coordinates and returns two lists, one
    randomXlist = []                   # with x coordinate and one with y coordinates
    randomYlist = []
    for i in range (1, 6):
        xi = random.randrange(1, 250)
        randomXlist.append(xi)
        yi = random.randrange(1, 250)
        randomYlist.append(yi)
        print ('x', i, ':', xi, sep='')
        print ('y', i, ':', yi, sep='')
        print ('\n')
    print('x:', randomXlist)
    print('y:', randomYlist)
    return[randomXlist,randomYlist]

def calculateDistance(x1, y1, x2, y2):                 #calculates distance between two given (x,y) coordinates
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  #and returns positive value
    print(round(dist,))
    return round(dist,)

def calculateRoadsDistance():  #jest na razie brzydko, bo na chama, ale działa. Można to potem inaczej zaimplementować
    coordinateList = randomCityGenerator()
    print('\n')
    # first [] 0 is the x list, 1 is the y list, second [] 0-4, elements of given list

    x1 = coordinateList[0][0]
    x2 = coordinateList[0][1]
    x3 = coordinateList[0][2]
    x4 = coordinateList[0][3]
    x5 = coordinateList[0][4]

    y1 = coordinateList[1][0]
    y2 = coordinateList[1][1]
    y3 = coordinateList[1][2]
    y4 = coordinateList[1][3]
    y5 = coordinateList[1][4]

    # All paths from point (x1,y1)
    AB = calculateDistance(x1, y1, x2, y2)
    AC = calculateDistance(x1, y1, x3, y3)
    AD = calculateDistance(x1, y1, x4, y4)
    AE = calculateDistance(x1, y1, x5, y5)

    # # All paths from point (x2,y2), some paths already calculated in previous steps
    BC = calculateDistance(x2, y2, x3, y3)
    BD = calculateDistance(x2, y2, x4, y4)
    BE = calculateDistance(x2, y2, x5, y5)

    # # All paths from point (x3,y3), some paths already calculated in previous steps
    CD = calculateDistance(x3, y3, x4, y4)
    CE = calculateDistance(x3, y3, x5, y5)

    # # All paths from point (x4,y4), some paths already calculated in previous steps
    DE = calculateDistance(x4, y4, x5, y5)
    return (AB, AC, AD, AE, BC, BD, BE, CD, CE, DE)


calculateRoadsDistance()

#def main():

