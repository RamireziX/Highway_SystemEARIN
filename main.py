from graph import *


def main():
   
    print("Write the value of w1 and press enter: ")
    w1 = input()
    print("w1 = " + w1)
    print("Write the value of w2 and press enter: ")
    w2 = input()
    print("w2 = " + w2)
    # python reads input as string
    w1 = float(w1)
    w2 = float(w2)
    
    if w1 < 0 or w1 > 1 or w2 < 0 or w2 > 1:
        print("\n ERROR! Invalid value of parameter detected. Please choose values between 0 and 1 for both w1 and w2.")
        exit()
        
    listOfCities = randomCityGenerator()
    path_costs = calculateRoadsDistance(listOfCities)
    w_graph = addWeights(path_costs, listOfCities)

    print('Adjacency matrix representing graph:')
    w_graph.print_adj_mat()

    best_graph = optimiseGraph(w_graph, w1, w2)
    print('BEST Adjacency matrix representing graph after optimising:')
    for row in best_graph:
        print(row)


main()
