import networkx as nx
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.pyplot as plt
import numpy
import numpy as np
import pylab

if __name__ == "__main__":

    def refreshGraph():
        plt.clf()
        nx.draw_networkx_nodes(T, pos, node_color='k', node_size=100, alpha=0.8)
        # nx.draw_networkx_nodes(T, pos, nodelist=white, node_color='w', node_size=100, alpha=0.8)
        nx.draw_networkx_edges(T, pos, width=1.0, alpha=0.5)
        plt.axis('on')
        plt.axis((-math.ceil(M/2), math.ceil(M/2), -math.ceil(N/2), math.ceil(N/2)))
        fig.patch.set_facecolor('white')
        plt.show()


    def onClick(event):
        (x, y) = (event.xdata, event.ydata)

        for i in allNodes:
            node = pos[i]
            distance = pow(x - node[0], 2) + pow(y - node[1], 2)
            if distance < 0.1:
                T.remove_node(i)
                allNodes.remove(i)
                refreshGraph()


    fig, ax = plt.subplots()
    fig.canvas.mpl_connect('button_press_event', onClick)

    T = nx.Graph()

    M, N = 10, 5
    ### Nodes
    checkpoints, start_finish = [], []
    allNodes = list(range(M*N))
    for i in range(M):
        for j in range(N):
            allNodes[i*M + j] = (i, j)

    for node in allNodes:
        T.add_node(node)

    ### Edges
    for i in range(1, M-1):
        for j in range(1, N-1):
            T.add_edge((i, j), (i - 1, j - 1))
            T.add_edge((i, j), (i - 1, j))
            T.add_edge((i, j), (i - 1, j + 1))
            T.add_edge((i, j), (i, j + 1))
            T.add_edge((i, j), (i + 1, j + 1))
            T.add_edge((i, j), (i + 1, j))
            T.add_edge((i, j), (i + 1, j - 1))
            T.add_edge((i, j), (i, j - 1))

    for i in range(1, M-1):
        T.add_edge((i, 0), (i - 1, 0))
        T.add_edge((i, 0), (i + 1, 0))
        T.add_edge((i, N-1), (i - 1, N-1))
        T.add_edge((i, N-1), (i + 1, N-1))

    for i in range(1, N-1):
        T.add_edge((0, i), (0, i - 1))
        T.add_edge((0, i), (0, i + 1))
        T.add_edge((N-1, i), (N-1, i - 1))
        T.add_edge((N-1, i), (N-1, i + 1))


    ### Positions of the nodes
    pos = {}
    for i in range(M):
        for j in range(N):
            pos[(i, j)] = numpy.array([i, j])
            print((i*M + j, [i, j]))

    ### Draw nodes and edges
    refreshGraph()

# def onClick():
#
#
# def __init__():
#     G = nx.Graph()
#     G.add_nodes_from([2, 3, 4, 5, 6])
#     G.add_edge(1, 2)
#     G.add_edge(1, 3)
#     G.add_edge(1, 4)
#     G.add_edge(1, 5)
#     # nx.draw(G)
#     # nx.draw_random(G)
#     # nx.draw_circular(G)
#     nx.draw_spectral(G)
#     plt.show()
#     fig, ax = plt.subplots()
#     fig.canvas.mpl_connect('button_press_event', onClick)
#
# if __name__ == "__main__":
#     __init__()