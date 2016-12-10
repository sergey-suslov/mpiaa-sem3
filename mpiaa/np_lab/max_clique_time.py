from mpiaa.np.max_clique import max_clique
from mpiaa.graphs.graph import Graph
from mpiaa.timer import time_us


def gen_full_graph(n):
    graph = Graph()
    for i in range(n):
        for j in range(i, n):
            graph.add_edge(i, j)
    return graph


if __name__ == "__main__":
    time_us({
        "Max clique": max_clique,
    }, ns=range(11), generator=gen_full_graph, repeats=10)

