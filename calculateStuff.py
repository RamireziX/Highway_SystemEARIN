import random
import math


class City:
    """Contains coordinates and id of a city"""

    def __init__(self, cityId, x, y):
        self.id = cityId
        self.x = x
        self.y = y


def randomCityGenerator():  # creates x cities, asks user for random or manual mode
    listOfCities = []

    print("Input '1' for randomly generated cities or '2' for custom coordinates: ")
    mode = input()
    mode = int(mode)
    if mode != 1 and mode != 2:
        print("\n ERROR! Please choose 1 for random mode and 2 for manual mode.")
        exit()

    elif mode == 1:  # RANDOM MODE
        # random.seed(0) # uncomment to use the same seed each time
        print("Choose number of cities (3-50): ")
        number = input()
        number = int(number)
        if number < 3 or number > 50:
            print("\n ERROR! Number of cities should be in the range 3-50.")
            exit()

        for i in range(1, number + 1):
            xi = random.randrange(1, 250)
            yi = random.randrange(1, 250)
            newCity = City(i, xi, yi)
            listOfCities.append(newCity)


    elif mode == 2:  # MANUAL MODE
        print("Choose number of cities (3-50): ")
        number = input()
        number = int(number)
        if number < 3 or number > 50:
            print("\n ERROR! Number of cities should be in the range 3-50.")
            exit()

        for i in range(1, number + 1):
            print("\nPlease choose x{}".format(i), "coordinate:")
            xi = input()
            xi = int(xi)
            if xi < 1 or xi > 250:
                print("\n ERROR! Please choose x and y values in range 1 to 250.")
                exit()
            print("\nPlease choose y{}".format(i), "coordinate:")
            yi = input()
            yi = int(yi)
            if yi < 1 or yi > 250:
                print("\n ERROR! Please choose x and y values in range 1 to 250.")
                exit()
            newCity = City(i, xi, yi)
            listOfCities.append(newCity)

    return listOfCities


def calculateDistance(x1, y1, x2, y2):  # calculates distance between two given (x,y) coordinates
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # and returns positive value
    return round(dist, )


# creates roads between cities and returns a list of them
def calculateRoadsDistance(listOfCities):
    noOfCities = len(listOfCities)
    listOfPaths = []
    for i in range(0, noOfCities):
        for j in range(i + 1, noOfCities):
            path = calculateDistance(listOfCities[i].x, listOfCities[i].y,
                                     listOfCities[j].x, listOfCities[j].y)
            listOfPaths.append(path)

    return listOfPaths


# heuristic (objective) function calculation
def calcHeuristicFunction(w1, w2, w_graph):
    allPaths = []
    # get all weights from graph
    for i in range(0, len(w_graph.nodes)):
        for j in range(i + 1, len(w_graph.nodes)):
            path = w_graph.get_weight(i, j)
            allPaths.append(path)
    # f(x) = w1*t(x) + w2*d(x)
    heuristic = w1 * calcTotalLength(allPaths) + w2 * calcAvgLength(w_graph)
    return heuristic


# sum of all roads
def calcTotalLength(allPaths):
    totalLength = sum(list(allPaths))
    return totalLength


# calculate average distance between 2 cities using dijkstra's algo
def calcAvgLength(w_graph):
    # list of distances between cities by dijkstra's algo
    total_distances = []
    # calculate shortest path to all cities from all cities
    for i in range(0, len(w_graph.nodes)):
        nodenum = w_graph.get_index_from_node(i)
        # Make a list keeping track of distance from city to any city
        # in self.nodes. Initialize to infinity for all city but the starting one
        dist = [None] * len(w_graph.nodes)
        for i in range(len(dist)):
            dist[i] = float("inf")

        dist[nodenum] = 0
        # Queue of all city in the graph
        queue = [i for i in range(len(w_graph.nodes))]
        # Set of cities seen so far
        seen = set()
        while len(queue) > 0:
            # Get city in queue that has not yet been seen
            # that has smallest distance to starting node
            min_dist = float("inf")
            min_node = None
            for n in queue:
                if dist[n] < min_dist and n not in seen:
                    min_dist = dist[n]
                    min_node = n

            # Add min distance city to seen, remove from queue
            queue.remove(min_node)
            seen.add(min_node)
            # Get all next hops
            connections = w_graph.connections_from(min_node)
            # For each connection, update its path and total distance from
            # starting city if the total distance is less than the current distance
            # in dist list, and add distance to the list of distances
            for (node, weight) in connections:
                tot_dist = weight + min_dist
                if tot_dist < dist[node.index]:
                    dist[node.index] = tot_dist
                    total_distances.append(tot_dist)

    # calculate average
    avgLength = sum(list(total_distances)) / len(total_distances)
    return avgLength
