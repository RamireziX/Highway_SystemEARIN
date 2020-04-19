import os
from calculateStuff import *
from graph import Node
from graph import Graph


def main():
    path_costs = calculateRoadsDistance()

    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")

    w_graph = Graph.create_from_nodes([a, b, c, d, e])

    w_graph.connect(a, b, path_costs[0])
    w_graph.connect(a, c, path_costs[1])
    w_graph.connect(a, d, path_costs[2])
    w_graph.connect(a, e, path_costs[3])
    w_graph.connect(b, c, path_costs[4])
    w_graph.connect(b, d, path_costs[5])
    w_graph.connect(b, e, path_costs[6])
    w_graph.connect(c, d, path_costs[7])
    w_graph.connect(c, e, path_costs[8])
    w_graph.connect(d, e, path_costs[9])

    print('Adjacency matrix representing graph:')
    w_graph.print_adj_mat()

    heuristic = calcHeuristicFunction(1, 1, calcTotalLength(), calcAvgLength())

    print('Value of heuristic function:')
    print(heuristic)


main()
