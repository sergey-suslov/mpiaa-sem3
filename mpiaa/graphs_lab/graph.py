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
        if v1 not in v2_adj:
            v2_adj.append(v1)

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

    def get_ostov_minimal_weight(self):
        full_weight = 0
        min_weight = maxsize
        min_vertex = object
        graph_size = len(self.vertices)
        avalable_vetrices = list()
        avalable_vetrices.append(next(iter(self.vertices)))
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





