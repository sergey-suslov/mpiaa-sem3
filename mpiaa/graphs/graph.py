class Graph(object):
    """Graph clas"""
    def __init__(self, vertices=[], edges=[]):
        self.vertices = set()
        self.adjacent = {}
        for v in vertices:
            self.add_vertex(v)
        for v1, v2 in edges:
            self.add_edge(v1, v2)

    def add_vertex(self, vertex):
        """Add vertex to the graph."""
        if vertex not in self.adjacent:
            self.adjacent[vertex] = []

    def add_edge(self, v1, v2):
        """Add edge (bidirectional) to the graph."""
        self.add_vertex(v1)
        self.add_vertex(v2)
        v1_adj = self.adjacent[v1]
        v2_adj = self.adjacent[v2]
        if v2 not in v1_adj:
            v1_adj.append(v2)
        if v1 not in v2_adj:
            v2_adj.append(v1)

    def get_adjacent(self, vertex):
        """Get list of adjacent vertices in the graph for the vertex"""
        if vertex in self.adjacent:
            return self.adjacent[vertex]
        return []



