class Graph(object):
    """Graph class"""
    def __init__(self, vertices=[], edges=[]):
        self.vertices = set()
        self.adjacent = {}
        for v in vertices:
            self.add_vertex(v)
        for v1, v2 in edges:
            self.add_edge(v1, v2)

    def add_vertex(self, vertex):
        """Add vertex to the graph."""
        self.vertices.add(vertex)
        """Add vertex to the graph."""
        if vertex not in self.adjacent:
            self.adjacent[vertex] = []

    def add_edge(self, v1, v2):
        """Add edge to the graph between vertices v1 and v2."""
        self.add_vertex(v1)
        self.add_vertex(v2)
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

    def has_edge(self, v1, v2):
        """Returns True if there is an edge between vertices v1 and v2, False otherwise."""
        if v1 not in self.vertices or v2 not in self.vertices:
            return False
        return v2 in self.adjacent[v1]



