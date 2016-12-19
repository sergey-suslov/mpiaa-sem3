import ctypes
import heapq
from tkinter import messagebox

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

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)



def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    path = [goal]+[came_from[goal]]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    return path[::-1]

def algorithm(graph, start, finish, checkpoints):
    result = []
    min_len = pylab.sys.maxsize
    min_path = []
    flag = True
    passed_point = start
    current_start = start
    while len(checkpoints) and flag:
        min_len = pylab.sys.maxsize
        min_path = []
        for i in checkpoints:
            is_valid = True
            try:
                path = a_star_search(graph, current_start, i)
            except:
                is_valid = False
                checkpoints.remove(i)
            if is_valid and len(path) < min_len:
                min_path = path
                min_len = len(path)
                passed_point = i
        result += min_path[1:]
        if len(checkpoints) == 1:
            flag = False
        if current_start in checkpoints:
            checkpoints.remove(current_start)
        current_start = passed_point
        if current_start in checkpoints:
            checkpoints.remove(current_start)
    try:
        path = a_star_search(graph, current_start, finish)
    except:
        messagebox.showinfo("Game message", "Path does not exist")
        return []
    result += path[1:]
    return [start] + result

if __name__ == "__main__":
    count = 0


    G = nx.Graph()
    M, N = 40, 10
    ### Nodes
    checkpoints, start_finish = [], []
    path_edges = []
    allNodes = list(range(M*N))




    def refreshGraph(edges_to_colorize=[], labels={}):
        plt.clf()
        nx.draw_networkx_nodes(G, pos, nodelist=allNodes, node_color='k', node_size=numpy.math.floor(3000/(M+N)), alpha=0.8)
        nx.draw_networkx_nodes(G, pos, nodelist=checkpoints, node_color='w', node_size=100, alpha=0.8)
        nx.draw_networkx_nodes(G, pos, nodelist=start_finish[:1], node_color='g', node_size=100, alpha=0.8)
        nx.draw_networkx_nodes(G, pos, nodelist=start_finish[1:], node_color='r', node_size=100, alpha=0.8)
        nx.draw_networkx_edges(G, pos, style='dotted', edge_color='k', width=1.0, alpha=0.7)
        nx.draw_networkx_edges(G, pos, edgelist=edges_to_colorize, edge_color='b', width=3.0, alpha=0.7)
        plt.axis('off')
        plt.axis((-1, M + 1, -1, N + 1))
        fig.patch.set_facecolor('white')
        plt.show()


    def bfs_paths(graph, start, goal):
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next in graph[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))

    def update_edges(nodes=[]):
        edges = []
        current_node = nodes[0]
        for i in nodes[1:]:
            edges.append((current_node, i))
            current_node = i
        refreshGraph(edges_to_colorize=edges)


    def onClick(event):
        (x, y) = (event.xdata, event.ydata)
        if event.button == 2:
            if len(start_finish) == 2:
                graph = G.adj
                g_key = graph[(1, 1)].keys()
                graph = {i: set([j for j in graph[i].keys()]) for i in graph.keys()}
                a = algorithm(G, start_finish[0], start_finish[1], checkpoints[:])
                update_edges(a)
            # setUp()
        else:
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
                        # G.remove_node(i)
                        for j in G.neighbors(i):
                            G.remove_edge(i, j)

                        # allNodes.remove(i)
                    refreshGraph()
                    # allNodes.remove(i)

                    # G.remove_node(i)
                    # allNodes.remove(i)
                    # refreshGraph()


    fig, ax = plt.subplots()
    fig.canvas.mpl_connect('button_press_event', onClick)

    counter = 0
    for i in range(M):
        for j in range(N):
            allNodes[counter] = (i, j)
            counter += 1

    for node in allNodes:
        G.add_node(node)

    ### Edges
    for i in range(1, M - 1):
        for j in range(1, N - 1):
            G.add_edge((i, j), (i - 1, j - 1))
            G.add_edge((i, j), (i - 1, j))
            G.add_edge((i, j), (i - 1, j + 1))
            G.add_edge((i, j), (i, j + 1))
            G.add_edge((i, j), (i + 1, j + 1))
            G.add_edge((i, j), (i + 1, j))
            G.add_edge((i, j), (i + 1, j - 1))
            G.add_edge((i, j), (i, j - 1))

    for i in range(1, M - 1):
        G.add_edge((i, 0), (i - 1, 0))
        G.add_edge((i, 0), (i + 1, 0))
        G.add_edge((i, N - 1), (i - 1, N - 1))
        G.add_edge((i, N - 1), (i + 1, N - 1))

    for i in range(1, N - 1):
        G.add_edge((0, i), (0, i - 1))
        G.add_edge((0, i), (0, i + 1))
        G.add_edge((M - 1, i), (M - 1, i - 1))
        G.add_edge((M - 1, i), (M - 1, i + 1))
    G.add_edge((1, 0), (0, 1))
    G.add_edge((M-2, 0), (M-1, 1))
    G.add_edge((M-2, N-1), (M-1, N-2))
    G.add_edge((0, N-2), (1, N-1))

    click_count = 0
    ### Positions of the nodes
    pos = {}
    for i in range(M):
        for j in range(N):
            pos[(i, j)] = numpy.array([i, j])
            print((i * M + j, [i, j]))

    def setUp():
        G.clear()
        for i in range(M):
            for j in range(N):
                allNodes[i * M + j] = (i, j)

        for node in allNodes:
            G.add_node(node)

        ### Edges
        for i in range(1, M - 1):
            for j in range(1, N - 1):
                G.add_edge((i, j), (i - 1, j - 1))
                G.add_edge((i, j), (i - 1, j))
                G.add_edge((i, j), (i - 1, j + 1))
                G.add_edge((i, j), (i, j + 1))
                G.add_edge((i, j), (i + 1, j + 1))
                G.add_edge((i, j), (i + 1, j))
                G.add_edge((i, j), (i + 1, j - 1))
                G.add_edge((i, j), (i, j - 1))

        for i in range(1, M - 1):
            G.add_edge((i, 0), (i - 1, 0))
            G.add_edge((i, 0), (i + 1, 0))
            G.add_edge((i, N - 1), (i - 1, N - 1))
            G.add_edge((i, N - 1), (i + 1, N - 1))

        for i in range(1, N - 1):
            G.add_edge((0, i), (0, i - 1))
            G.add_edge((0, i), (0, i + 1))
            G.add_edge((N - 1, i), (N - 1, i - 1))
            G.add_edge((N - 1, i), (N - 1, i + 1))

        click_count = 0
        ### Positions of the nodes
        pos = {}
        for i in range(M):
            for j in range(N):
                pos[(i, j)] = numpy.array([i, j])
                print((i * M + j, [i, j]))
        refreshGraph()
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