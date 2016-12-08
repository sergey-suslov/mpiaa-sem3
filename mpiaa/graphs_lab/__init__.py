from random import random

import time

import sys

from mpiaa.graphs_lab.graph_algs import shortest_path
from mpiaa.graphs_lab.bellman import bellman_ford
from mpiaa.graphs_lab.graph import Graph
from mpiaa.graphs_lab import StrongConnectivity, DFS


def practise():
    lab_graph = Graph()
    with open('src/graph.txt') as graph_file:
        graph_file = graph_file.read()
        for adj in graph_file.split('\n')[:150000]:
            pair = adj.split('\t')
            lab_graph.add_edge(str(pair[0]), str(pair[1]), int(100*random()))
    graph_dict = lab_graph.adjacent
    t1 = time.time()
    lab_graph.get_ostov_minimal_weight()
    t2 = time.time()
    print("Ostov " + str(t2 - t1))
    print("Graph is filled")
    #Bellman-Floyd########################################
    print(shortest_path(lab_graph, "9907233"))
    ######################################################
    #Custom Sedgwick#######################################
    t1 = time.time()
    components = lab_graph.kosaraju()
    t2 = time.time()
    num_of_comps = len(components)
    print("Strongy connected components kosaraju " + str(t2 - t1) + " num of comps: " + str(num_of_comps))
    ######################################################

    #Lib Sedgwick##########################################
    t1 = time.time()
    components = StrongConnectivity.Condensation(graph_dict)
    t2 = time.time()
    num_of_comps = len(components)
    sum = 0
    min_len = sys.maxsize
    max_len = 0
    for i in components:
        current_len = len(i)
        sum+= current_len
        if  current_len > max_len:
            max_len = current_len
        if current_len < min_len:
            min_len = current_len
    average_len = sum / num_of_comps
    print("Strongy connected components lib's " + str(t2 - t1) + " num of comps: " + str(num_of_comps))
    print("min, max, average length of components: " + str(min_len) + ", " + str(max_len) + ", " + str(average_len))
    ######################################################

    #Ostov################################################
    print("Ostov " + str(lab_graph.get_ostov_minimal_weight()))
    ######################################################

if __name__ == "__main__":
    practise()
