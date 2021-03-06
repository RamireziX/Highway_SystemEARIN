from calculateStuff import *
from copy import deepcopy


class Node:

    def __init__(self, data, indexloc=None):
        self.data = data
        self.index = indexloc


class Graph:

    @classmethod
    def create_from_nodes(self, nodes):
        return Graph(len(nodes), len(nodes), nodes)

    def __init__(self, row, col, nodes=None):
        # set up an adjacency matrix
        self.adj_mat = [[0] * col for _ in range(row)]
        self.nodes = nodes
        for i in range(len(self.nodes)):
            self.nodes[i].index = i

    # Conncects from node1 to node2
    # row is source, column is destination
    def connect_dir(self, node1, node2, weight=1):
        node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
        self.adj_mat[node1][node2] = weight

    # Optional weight argument, by default set to 1
    def connect(self, node1, node2, weight=1):
        self.connect_dir(node1, node2, weight)
        self.connect_dir(node2, node1, weight)

    # Get node row, map non-zero items to their node in the self.nodes array
    # Select any non-zero elements, leaving you with an array of nodes
    # which are connections_to (for a directed graph)
    # Return value: array of tuples (node, weight)
    def connections_from(self, node):
        node = self.get_index_from_node(node)
        return [(self.nodes[col_num], self.adj_mat[node][col_num]) for col_num in range(len(self.adj_mat[node])) if
                self.adj_mat[node][col_num] != 0]

    # Map matrix to column of node
    # Map any non-zero elements to the node at that row index
    # Select only non-zero elements
    # Note for a non-directed graph, you can use connections_to OR
    # connections_from
    # Return value: array of tuples (node, weight)
    def connections_to(self, node):
        node = self.get_index_from_node(node)
        column = [row[node] for row in self.adj_mat]
        return [(self.nodes[row_num], column[row_num]) for row_num in range(len(column)) if column[row_num] != 0]

    def print_adj_mat(self):
        for row in self.adj_mat:
            print(row)

    def node(self, index):
        return self.nodes[index]

    def remove_conn(self, node1, node2):
        self.remove_conn_dir(node1, node2)
        self.remove_conn_dir(node2, node1)

    # Remove connection in a directed manner (nod1 to node2)
    # Can accept index number OR node object
    def remove_conn_dir(self, node1, node2):
        node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
        self.adj_mat[node1][node2] = 0

    # Can go from node 1 to node 2?
    def can_traverse_dir(self, node1, node2):
        node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
        return self.adj_mat[node1][node2] != 0

    def has_conn(self, node1, node2):
        return self.can_traverse_dir(node1, node2) or self.can_traverse_dir(node2, node1)

    def add_node(self, node):
        self.nodes.append(node)
        node.index = len(self.nodes) - 1
        for row in self.adj_mat:
            row.append(0)
        self.adj_mat.append([0] * (len(self.adj_mat) + 1))

    # Get the weight associated with travelling from n1
    # to n2. Can accept index numbers OR node objects
    def get_weight(self, n1, n2):
        node1, node2 = self.get_index_from_node(n1), self.get_index_from_node(n2)
        return self.adj_mat[node1][node2]

    # Allows either node OR node indices to be passed into
    def get_index_from_node(self, node):
        if not isinstance(node, Node) and not isinstance(node, int):
            raise ValueError("node must be an integer or a Node object")
        if isinstance(node, int):
            return node
        else:
            return node.index


# add weights from calculated road distances
def addWeights(path_costs, listOfCities):
    listOfNodes = []
    noOfCities = len(listOfCities)
    for i in range(0, noOfCities):
        node = Node(i + 1)
        listOfNodes.append(node)

    w_graph = Graph.create_from_nodes(listOfNodes)
    k = 0
    for i in range(0, noOfCities):
        for j in range(i + 1, noOfCities):
            w_graph.connect(listOfNodes[i], listOfNodes[j], path_costs[k])
            k = k + 1

    return w_graph


# a* algorithm
def optimiseGraph(w_graph, w1, w2):
    listOfGraphs = []
    listOfHeuristics = []
    for i in range(0, len(w_graph.nodes)):
        for j in range(i + 1, len(w_graph.nodes)):
            # check, if graph is still connected - at least one value in a row is non zero
            nonZeroVertices = []
            for k in range(0, len(w_graph.nodes)):
                vertice = w_graph.adj_mat[i][k]
                if vertice != 0:
                    nonZeroVertices.append(vertice)
            # delete one vertice
            if len(nonZeroVertices) > 1:
                # to be sure 1st graph with all vertices is included
                # (can be a result if w1 ~= 0 w2 = 1)
                if i == 0 and j == 1:
                    # save graph as adj matrix
                    newAdjMat = deepcopy(w_graph.adj_mat)
                    heuristic = calcHeuristicFunction(w1, w2, w_graph)
                    listOfGraphs.append(newAdjMat)
                    listOfHeuristics.append(heuristic)
                w_graph.remove_conn(i, j)
                # save graph as adj matrix
                newAdjMat = deepcopy(w_graph.adj_mat)
                heuristic = calcHeuristicFunction(w1, w2, w_graph)
                listOfGraphs.append(newAdjMat)
                listOfHeuristics.append(heuristic)

    # get index of smallest value of heuristic, which is shared by best graph
    index_min = min(range(len(listOfHeuristics)), key=listOfHeuristics.__getitem__)
    print('------------------------RESULT---------------------------')
    print("Best heuristic = " + str(listOfHeuristics[index_min]))
    return listOfGraphs[index_min]
