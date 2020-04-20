from calculateStuff import *
from graph import *


def main():
    listOfCities = randomCityGenerator()
    path_costs = calculateRoadsDistance(listOfCities)
    w_graph = addWeights(path_costs, listOfCities)

    print('Adjacency matrix representing graph:')
    w_graph.print_adj_mat()

    heuristic = calcHeuristicFunction(1, 1, calcTotalLength(path_costs), calcAvgLength(path_costs))

    print('Value of heuristic function:')
    print(heuristic)


main()
