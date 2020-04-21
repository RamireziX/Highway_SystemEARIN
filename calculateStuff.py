import random
import math


class City:
    """Contains coordinates and id of a city"""

    def __init__(self, cityId, x, y):
        self.id = cityId
        self.x = x
        self.y = y


def randomCityGenerator():  # creates 5 cities with random coordinates
    listOfCities = []
    # print('Random coordinates for all cities:')
    random.seed(0)  # THIS WILL STOP RANDOM EXECUTION EACH TIME AND SAVE ONE STATE,
    for i in range(1, 6):  # FOR THE PURPOSE OF TESTING, Remove to make program use different
        xi = random.randrange(1, 250)  # numbers each time
        yi = random.randrange(1, 250)
        newCity = City(i, xi, yi)
        listOfCities.append(newCity)

    return listOfCities


def calculateDistance(x1, y1, x2, y2):  # calculates distance between two given (x,y) coordinates
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # and returns positive value
    # print(round(dist, ))
    return round(dist, )


def calculateRoadsDistance(listOfCities):
    noOfCities = len(listOfCities)
    listOfPaths = []
    for i in range(0, noOfCities):
        for j in range(i + 1, noOfCities):
            path = calculateDistance(listOfCities[i].x, listOfCities[i].y,
                                     listOfCities[j].x, listOfCities[j].y)
            listOfPaths.append(path)

    return listOfPaths


def calcHeuristicFunction(w1, w2, w_graph, noOfCities):  # noOfCities mozna wczesniej policzyc i miec jako jakis
    # global variable czy cos, bo liczba miast sie nie bedzie zmieniac
    allPaths = []
    # get all weights from graph
    for i in range(0, noOfCities):
        for j in range(i + 1, noOfCities):
            path = w_graph.get_weight(i, j)
            allPaths.append(path)

    heuristic = w1 * calcTotalLength(allPaths) + w2 * calcAvgLength(allPaths)
    return heuristic


def calcTotalLength(allPaths):
    totalLength = sum(list(allPaths))
    return totalLength


def calcAvgLength(allPaths):
    avgLength = sum(list(allPaths)) / len(allPaths)
    return avgLength
