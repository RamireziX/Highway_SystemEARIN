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
    print(randomXlist)
    print(randomYlist)

def calculateDistance(x1, y1, x2, y2):     #calculates distance between two given (x,y) coordinates
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


#def main():
randomCityGenerator()


