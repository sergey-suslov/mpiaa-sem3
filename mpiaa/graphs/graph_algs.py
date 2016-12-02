import operator

import mpiaa.graphs.graph
import sys

def is_connected(graph):
    """Returns True if graph is connected, otherwise False"""
    passed = {key: False for key in graph.get_vertices()}
    start_vertex = list(passed)[0]
    passed[start_vertex] = True
    bypassing_deep_connected(graph, start_vertex, passed)
    for vertex in passed:
        if not passed.get(vertex):
            return False
    return True

def bypassing_deep_connected(graph, vertex, passed):
    for v in graph.get_adjacent(vertex):
        if not passed[v]:
            passed[v] = True
            bypassing_deep_connected(graph, v, passed)

def shortest_path(graph, src_vertex, dest_vertex):
    """Returns shortest path between src and dest vertices in the graph.
    Shortest path is returned as list [src_vertex, ..., dest_vertex].
    If there is no path, returns empty list."""
    return dijkstra(graph, src_vertex, dest_vertex)



def bypassing_deep(g, vertex, passed, color, list_of_components):
    list_of_components[color].append(vertex)
    for v in g.get_adjacent(vertex):
        if not passed[v]:
            passed[v] = True
            bypassing_deep(g, v, passed, color, list_of_components)


def connected_components(graph):
    """Returns all connected components of the graph as list of lists of vertices."""
    color = 0
    passed = {key: False for key in graph.get_vertices()}
    list_of_components = [[]]
    for v in graph.get_vertices():
        if not passed[v]:
            passed[v] = True
            bypassing_deep(graph, v, passed, color, list_of_components)
            color += 1
            list_of_components.append([])

    return list_of_components[:-1]


def find_min_vertex(lst, is_visited_lst):
    length = len(lst)
    n = 0
    while n < length:
        min_index = min(lst, key=lambda k: lst[k])
        if not is_visited_lst[str(min_index)]:
            return min_index
        else:
            lst[min_index] = sys.maxsize
        n += 1
    return None


def dijkstra(g, s, v):
    graph_len = len(g.get_vertices())
    d = {key: sys.maxsize for key in g.get_vertices()}
    d[s] = 0
    p = {key: None for key in g.get_vertices()}
    p[s] = s
    u = {key: False for key in g.get_vertices()}
    #min_index, min_value = min(enumerate(), key=operator.itemgetter(1))
    n = 0
    while n <= graph_len:
        min_vertex = find_min_vertex(d.copy(), u)
        if min_vertex == None:
            break
        u[min_vertex] = True
        adj = g.get_adjacent(min_vertex)
        for edge in adj:
            if d[edge] > d[min_vertex] + 1:
                d[edge] = d[min_vertex] + 1
                p[edge] = min_vertex
        n += 1

    if not p[v]:
        return []
    path = [v]
    while path[-1] != s:
        path.append(p[path[-1]])
    return path[::-1]

#
# def dijkstra(g, s, v):
#     graph_len = len(g.get_vertices())
#     d = [sys.maxsize]*graph_len
#     d[s] = 0
#     p = [None]*graph_len
#     p[0] = 0
#     u = [False]*graph_len
#     #min_index, min_value = min(enumerate(), key=operator.itemgetter(1))
#     n = 0
#     while n <= graph_len:
#         min_vertex = find_min_vertex(d[:], u)
#         if min_vertex == None:
#             break
#         u[min_vertex] = True
#         adj = g.get_adjacent(min_vertex)
#         for edge in adj:
#             if d[edge] > d[min_vertex] + 1:
#                 d[edge] = d[min_vertex] + 1
#                 p[edge] = min_vertex
#
#     path = [v]
#     while path[-1] != s:
#         path.append(p[path[-1]])
#     return path
