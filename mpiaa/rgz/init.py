import networkx as nx
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.pyplot as plt
import numpy
import numpy as np
import pylab


class ClickCount:

    click_count = 0

    def init(self):
        pass

    def get(self):
        self.click_count

    def increase(self):
        self.click_count += 1

if __name__ == "__main__":

    T = nx.Graph()
    M, N = 10, 10
    ### Nodes
    checkpoints, start_finish = [], []
    allNodes = list(range(M*N))
    count = 0


    def refreshGraph():
        plt.clf()
        nx.draw_networkx_nodes(T, pos, nodelist=allNodes, node_color='k', node_size=100, alpha=0.8)
        nx.draw_networkx_nodes(T, pos, nodelist=checkpoints, node_color='w', node_size=100, alpha=0.8)
        nx.draw_networkx_nodes(T, pos, nodelist=start_finish[:1], node_color='g', node_size=100, alpha=0.8)
        nx.draw_networkx_nodes(T, pos, nodelist=start_finish[1:], node_color='r', node_size=100, alpha=0.8)
        nx.draw_networkx_edges(T, pos, edge_color='k', width=1.0, alpha=0.5)
        plt.axis('on')
        plt.axis((-1, N, -1, M))
        fig.patch.set_facecolor('white')
        plt.show()




    def onClick(event):
        (x, y) = (event.xdata, event.ydata)
        for i in allNodes:
            node = pos[i]
            distance = pow(x - node[0], 2) + pow(y - node[1], 2)
            if distance < 0.1:
                if event.button == 1:
                    if len(start_finish) == 0:
                        start_finish.append(i)
                    elif len(start_finish) == 1:
                        start_finish.append(i)
                    else:
                        if i in checkpoints:
                            checkpoints.remove(i)
                        else:
                            checkpoints.append(i)
                elif event.button == 3:
                    # allNodes.remove(i)
                    # T.remove_node(i)
                    for j in T.neighbors(i):
                        T.remove_edge(i, j)
                elif event.button == 2:
                    setUp()
                    # allNodes.remove(i)
                refreshGraph()
                    # allNodes.remove(i)

                    # T.remove_node(i)
                    # allNodes.remove(i)
                    # refreshGraph()


    fig, ax = plt.subplots()
    fig.canvas.mpl_connect('button_press_event', onClick)

    for i in range(M):
        for j in range(N):
            allNodes[i * M + j] = (i, j)

    for node in allNodes:
        T.add_node(node)

    ### Edges
    for i in range(1, M - 1):
        for j in range(1, N - 1):
            T.add_edge((i, j), (i - 1, j - 1))
            T.add_edge((i, j), (i - 1, j))
            T.add_edge((i, j), (i - 1, j + 1))
            T.add_edge((i, j), (i, j + 1))
            T.add_edge((i, j), (i + 1, j + 1))
            T.add_edge((i, j), (i + 1, j))
            T.add_edge((i, j), (i + 1, j - 1))
            T.add_edge((i, j), (i, j - 1))

    for i in range(1, M - 1):
        T.add_edge((i, 0), (i - 1, 0))
        T.add_edge((i, 0), (i + 1, 0))
        T.add_edge((i, N - 1), (i - 1, N - 1))
        T.add_edge((i, N - 1), (i + 1, N - 1))

    for i in range(1, N - 1):
        T.add_edge((0, i), (0, i - 1))
        T.add_edge((0, i), (0, i + 1))
        T.add_edge((N - 1, i), (N - 1, i - 1))
        T.add_edge((N - 1, i), (N - 1, i + 1))

    click_count = 0
    ### Positions of the nodes
    pos = {}
    for i in range(M):
        for j in range(N):
            pos[(i, j)] = numpy.array([i, j])
            print((i * M + j, [i, j]))

    def setUp():
        for i in range(M):
            for j in range(N):
                allNodes[i * M + j] = (i, j)

        for node in allNodes:
            T.add_node(node)

        ### Edges
        for i in range(1, M - 1):
            for j in range(1, N - 1):
                T.add_edge((i, j), (i - 1, j - 1))
                T.add_edge((i, j), (i - 1, j))
                T.add_edge((i, j), (i - 1, j + 1))
                T.add_edge((i, j), (i, j + 1))
                T.add_edge((i, j), (i + 1, j + 1))
                T.add_edge((i, j), (i + 1, j))
                T.add_edge((i, j), (i + 1, j - 1))
                T.add_edge((i, j), (i, j - 1))

        for i in range(1, M - 1):
            T.add_edge((i, 0), (i - 1, 0))
            T.add_edge((i, 0), (i + 1, 0))
            T.add_edge((i, N - 1), (i - 1, N - 1))
            T.add_edge((i, N - 1), (i + 1, N - 1))

        for i in range(1, N - 1):
            T.add_edge((0, i), (0, i - 1))
            T.add_edge((0, i), (0, i + 1))
            T.add_edge((N - 1, i), (N - 1, i - 1))
            T.add_edge((N - 1, i), (N - 1, i + 1))

        click_count = 0
        ### Positions of the nodes
        pos = {}
        for i in range(M):
            for j in range(N):
                pos[(i, j)] = numpy.array([i, j])
                print((i * M + j, [i, j]))
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