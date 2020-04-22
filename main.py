from calculateStuff import *
from graph import *


def main():
    listOfCities = randomCityGenerator()
    noOfCities = len(listOfCities)
    path_costs = calculateRoadsDistance(listOfCities)
    w_graph = addWeights(path_costs, listOfCities)

    print('Adjacency matrix representing graph:')
    w_graph.print_adj_mat()

    best_graph = optimiseGraph(w_graph, noOfCities)
    print('BEST Adjacency matrix representing graph after optimising:')
    for row in best_graph:
        print(row)


main()
