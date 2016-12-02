from mpiaa.graphs.graph import Graph
from mpiaa.graphs.graph_algs import dijkstra


def practise():
    lab_graph = Graph()
    with open('../../record_gen/graph') as graph_file:
        graph_file = graph_file.read()
        for adj in graph_file.split('\n'):
            pair = adj.split(' ')
            lab_graph.add_edge(str(pair[0]), str(pair[1]))
    print(dijkstra(lab_graph, '2', '118'))


if __name__ == "__main__":
    practise()
