import random
import math

def randomCityGenerator():             # creates 5 random (x,y) coordinates and returns two lists, one
    randomXlist = []                   # with x coordinate and one with y coordinates
    randomYlist = []
    print('Random coordinates for all cities:')
    random.seed(0)                      # THIS WILL STOP RANDOM EXECUTION EACH TIME AND SAVE ONE STATE,
    for i in range (1, 6):              # FOR THE PURPOSE OF TESTING, Remove to make program use different
        xi = random.randrange(1, 250)   # numbers each time
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

    print("Cost of all paths:")
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

    print('\n')
    return (AB, AC, AD, AE, BC, BD, BE, CD, CE, DE)


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
    # Note row is source, column is destination
    # Allows weighted edges
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





path_costs = calculateRoadsDistance()

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")

w_graph = Graph.create_from_nodes([a,b,c,d,e])

w_graph.connect(a,b,path_costs[0])
w_graph.connect(a,c,path_costs[1])
w_graph.connect(a,d,path_costs[2])
w_graph.connect(a,e,path_costs[3])
w_graph.connect(b,c,path_costs[4])
w_graph.connect(b,d,path_costs[5])
w_graph.connect(b,e,path_costs[6])
w_graph.connect(c,d,path_costs[7])
w_graph.connect(c,e,path_costs[8])
w_graph.connect(d,e,path_costs[9])

print('Adjacency matrix representing graph:')
w_graph.print_adj_mat()

#def main():

