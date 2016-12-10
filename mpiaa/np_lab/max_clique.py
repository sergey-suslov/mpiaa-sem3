import itertools

import copy


def is_clique(graph, vertices):
    """
    Checks that vertices form clique of the graph.

    :param graph: graph (object of Graph type)
    :param vertices: list of vertices of the graph
    :return: True if vertices are clique, otherwise False
    """
    if not vertices:
        return False
    # Replace by correct code
    def do_contain(small, big):
        for i in small:
            if not big.__contains__(i):
                return False
        return True

    for v in vertices:
        adj = graph.get_adjacent(v)
        adj.append(v)
        if not do_contain(vertices, adj):
            return False
    return True


def all_combinations(items):
    """
    Returns all combinations of different number of items.
    Includes all unique combinations of 1 item, 2 items, etc.

    :param items: list of items
    :return: list of lists, each list is a unique combination of given items
    """
    def binary_increase(d):
        for i in d:
            if i[1] == 0:
                i[1] = 1
                return True
            else:
                i[1] = 0
        return False
    def create_combination(l):
        temp_list = list()
        for i in l:
            if i[1] == 1:
                temp_list.append(i[0])
        return(temp_list)
    #dict_copy = {x: x for x in items}
    result = list()
    binary_list = [[x, 0] for x in items]
    while binary_increase(binary_list):
        result.append(create_combination(binary_list))
    # Replace by correct code
    return result


def max_clique(graph):
    """
    Returns max clique of the graph.

    :param graph: graph (object of type Graph)
    :return: max clique as list of vertices of the clique
    """
    t = list()
    potencial_clicues = all_combinations(graph.get_vertices())
    for i in potencial_clicues:
        if is_clique(graph, i):
            if len(t) < len(i):
                t = i
    return t
