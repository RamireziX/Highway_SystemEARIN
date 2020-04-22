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


def calcHeuristicFunction(w1, w2, w_graph, noOfCities):  # noOfCities mozna wczesniej policzyc
    # i miec jako jakis
    # global variable czy cos, bo liczba miast sie nie bedzie zmieniac
    allPaths = []
    # get all weights from graph
    for i in range(0, noOfCities):
        for j in range(i + 1, noOfCities):
            path = w_graph.get_weight(i, j)
            allPaths.append(path)

    heuristic = w1 * calcTotalLength(allPaths) + w2 * calcAvgLength(w_graph, noOfCities)
    return heuristic


def calcTotalLength(allPaths):
    totalLength = sum(list(allPaths))
    return totalLength


# to nie jest ok
# def calcAvgLength(allPaths):
#     avgLength = sum(list(allPaths)) / len(allPaths)
#     return avgLength

# to jest ok
def calcAvgLength(w_graph, noOfCities):
    # Get index of node (or maintain int passed in)
    onlyDistances = []
    for i in range(0, noOfCities):
        nodenum = w_graph.get_index_from_node(i)

        # Make an array keeping track of distance from node to any node
        # in self.nodes. Initialize to infinity for all nodes but the
        # starting node, keep track of "path" which relates to distance.
        # Index 0 = distance, index 1 = node hops
        dist = [None] * len(w_graph.nodes)
        for i in range(len(dist)):
            dist[i] = [float("inf")]
            dist[i].append([w_graph.nodes[nodenum]])

        dist[nodenum][0] = 0
        # Queue of all nodes in the graph
        # Note the integers in the queue correspond to indices of node
        # locations in the self.nodes array
        queue = [i for i in range(len(w_graph.nodes))]
        # Set of numbers seen so far
        seen = set()
        while len(queue) > 0:
            # Get node in queue that has not yet been seen
            # that has smallest distance to starting node
            min_dist = float("inf")
            min_node = None
            for n in queue:
                if dist[n][0] < min_dist and n not in seen:
                    min_dist = dist[n][0]
                    min_node = n

            # Add min distance node to seen, remove from queue
            queue.remove(min_node)
            seen.add(min_node)
            # Get all next hops
            connections = w_graph.connections_from(min_node)
            # For each connection, update its path and total distance from
            # starting node if the total distance is less than the current distance
            # in dist array
            for (node, weight) in connections:
                tot_dist = weight + min_dist
                if tot_dist < dist[node.index][0]:
                    dist[node.index][0] = tot_dist
                    onlyDistances.append(tot_dist)
                    dist[node.index][1] = list(dist[min_node][1])
                    dist[node.index][1].append(node)
    avgLength = sum(list(onlyDistances)) / len(onlyDistances)
    return avgLength
