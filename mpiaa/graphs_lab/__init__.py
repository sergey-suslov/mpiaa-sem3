from random import random

import time

from mpiaa.graphs_lab.graph import Graph
from mpiaa.graphs_lab import StrongConnectivity, DFS


def practise():
    lab_graph = Graph()
    with open('src/graph.txt') as graph_file:
        graph_file = graph_file.read()
        for adj in graph_file.split('\n')[:200000]:
            pair = adj.split('\t')
            lab_graph.add_edge(str(pair[0]), str(pair[1]), int(100*random()))
    graph_dict = {x: lab_graph.get_adjacent(x) for x in lab_graph.get_vertices()}
    print("Graph is filled")

    #Custom Sedgwick#######################################

    t1 = time.time()
    components = lab_graph.kosaraju()
    t2 = time.time()
    len_of_comps = len(components)
    print("Strongy connected components kosaraju " + str(t2 - t1) + " num of comps: " + str(len_of_comps))
    ######################################################

    #Lib Sedgwick##########################################
    t1 = time.time()
    components = StrongConnectivity.Condensation(graph_dict)
    t2 = time.time()
    len_of_comps = len(components)
    print("Strongy connected components lib's " + str(t2 - t1) + " num of comps: " + str(len_of_comps))
    ######################################################

    #Ostov################################################
    print("Ostov " + str(lab_graph.get_ostov_minimal_weight()))
    ######################################################

if __name__ == "__main__":
    practise()
