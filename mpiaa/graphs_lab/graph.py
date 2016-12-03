from collections import defaultdict
from sys import maxsize


class Graph(object):
    """Graph class"""
    def __init__(self, vertices=[], edges=[], weight={}):
        self.vertices = set()
        self.adjacent = {}
        self.weight = {}
        for v in vertices:
            self.add_vertex(v)
        for v1, v2 in edges:
            self.add_edge(v1, v2)
        for k, v in weight:
            self.weight[k] = v

    def add_vertex(self, vertex):
        """Add vertex to the graph."""
        self.vertices.add(vertex)
        """Add vertex to the graph."""
        if vertex not in self.adjacent:
            self.adjacent[vertex] = []

    def add_edge(self, v1, v2, weight=1):
        """Add edge to the graph between vertices v1 and v2."""
        self.add_vertex(v1)
        self.add_vertex(v2)
        if v1 in self.weight:
            self.weight[v1][v2] = weight
        else:
            self.weight[v1] = {}
            self.weight[v1][v2] = weight
        if v2 in self.weight:
            self.weight[v2][v1] = weight
        else:
            self.weight[v2] = {}
            self.weight[v2][v1] = weight
        v1_adj = self.adjacent[v1]
        v2_adj = self.adjacent[v2]
        if v2 not in v1_adj:
            v1_adj.append(v2)

    def get_vertices(self):
        """Get all vertices of the graph."""
        return list(self.vertices)

    def get_adjacent(self, vertex):
        """Get list of adjacent vertices in the graph for the vertex"""
        if vertex in self.adjacent:
            return self.adjacent[vertex]
        return []

    def get_weight(self, vertex):
        return self.weight[vertex]

    def has_edge(self, v1, v2):
        """Returns True if there is an edge between vertices v1 and v2, False otherwise."""
        if v1 not in self.vertices or v2 not in self.vertices:
            return False
        return v2 in self.adjacent[v1]

    def get_reverse_graph(self):
        reverse_graph = Graph()
        for v in self.vertices:
            for adj_v in self.adjacent[v]:
                reverse_graph.add_edge(adj_v, v)
        return  reverse_graph

    def get_ostov_minimal_weight(self):
        full_weight = 0
        min_weight = maxsize
        graph_size = len(self.vertices)
        avalable_vetrices = list()
        start_vertex = next(iter(self.vertices))
        min_vertex = start_vertex
        avalable_vetrices.append(start_vertex)
        while len(avalable_vetrices) != graph_size:
            for vertex in avalable_vetrices:
                for adj_vetrex in self.adjacent[vertex]:
                    if adj_vetrex not in avalable_vetrices:
                        current_weight = self.weight[vertex][adj_vetrex]
                        if current_weight < min_weight:
                            min_weight = current_weight
                            min_vertex = adj_vetrex
            full_weight += min_weight
            avalable_vetrices.append(min_vertex)
            min_weight = maxsize
        return full_weight
    #Ошибочка вышла
    # def get_strongly_connected_components(self):
    #     color_dict = {v: 0 for v in self.vertices}
    #
    #     def bypassing_deep(vertex, colour):
    #         for adj_vertex in self.adjacent[vertex]:
    #             if vertex in self.adjacent[adj_vertex] and color_dict[adj_vertex] == 0:
    #                 color_dict[adj_vertex] = colour
    #                 bypassing_deep(adj_vertex, colour)
    #     color = 1
    #     for k, v in color_dict.items():
    #         if v == 0:
    #             bypassing_deep(k, color)
    #         color += 1
    #     result = [[] for i in range(color)]
    #     for k, v in color_dict.items():
    #         result[v-1].append(k)
    #     return result

    def kosaraju(self):
        def first_pass(graph):
            seen = set()
            ordering = []

            def dfs(v):
                seen.add(v)
                for u in graph.adjacent[v]:
                    if u not in seen:
                        dfs(u)
                ordering.append(v)

            for u in graph.vertices:
                if u not in seen:
                    dfs(u)
            return ordering

        def second_pass(ordering):
            seen = set()
            leader = defaultdict(list)
            for u in reversed(ordering):
                if u not in seen:
                    # Non recursive DFS using a stack
                    seen.add(u)
                    stack = [u]
                    while stack:
                        item = stack.pop()
                        for v in self.adjacent[item]:
                            if v not in seen:
                                seen.add(v)
                                stack.append(v)
                        leader[u].append(item)
            return leader
        result = second_pass(first_pass(self.get_reverse_graph()))
        return [v for k, v in result.items()]