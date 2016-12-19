import networkx as nx
from django.utils import unittest
from mpiaa.rgz.init import algorithm


class Algorithm_test(unittest.TestCase):
    M, N = 40, 10
    ### Nodes
    checkpoints, start_finish = [], []
    path_edges = []
    allNodes = list(range(M * N))

    def setUp(self):
        self.G = nx.Graph()
        counter = 0
        for i in range(self.M):
            for j in range(self.N):
                self.allNodes[counter] = (i, j)
                counter += 1
        for node in self.allNodes:
            self.G.add_node(node)
        for i in range(1, self.M - 1):
            for j in range(1, self.N - 1):
                self.G.add_edge((i, j), (i - 1, j - 1))
                self.G.add_edge((i, j), (i - 1, j))
                self.G.add_edge((i, j), (i - 1, j + 1))
                self.G.add_edge((i, j), (i, j + 1))
                self.G.add_edge((i, j), (i + 1, j + 1))
                self.G.add_edge((i, j), (i + 1, j))
                self.G.add_edge((i, j), (i + 1, j - 1))
                self.G.add_edge((i, j), (i, j - 1))

        for i in range(1, self.M - 1):
            self.G.add_edge((i, 0), (i - 1, 0))
            self.G.add_edge((i, 0), (i + 1, 0))
            self.G.add_edge((i, self.N - 1), (i - 1, self.N - 1))
            self.G.add_edge((i, self.N - 1), (i + 1, self.N - 1))

        for i in range(1, self.N - 1):
            self.G.add_edge((0, i), (0, i - 1))
            self.G.add_edge((0, i), (0, i + 1))
            self.G.add_edge((self.M - 1, i), (self.M - 1, i - 1))
            self.G.add_edge((self.M - 1, i), (self.M - 1, i + 1))
        self.G.add_edge((1, 0), (0, 1))
        self.G.add_edge((self.M - 2, 0), (self.M - 1, 1))
        self.G.add_edge((self.M - 2, self.N - 1), (self.M - 1, self.N - 2))
        self.G.add_edge((0, self.N - 2), (1, self.N - 1))

    def test_no_checkpoints(self):
        start_finish = [(0, 0), (5, 5)]
        self.assertEqual(algorithm(self.G, start_finish[0], start_finish[1], self.checkpoints), [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])

    def test_one_checkpoint(self):
        start_finish = [(0, 0), (5, 5)]
        self.checkpoints = [(0, 5)]
        self.assertEqual(algorithm(self.G, start_finish[0], start_finish[1], self.checkpoints), [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)])

    def test_many_checkpoint(self):
        start_finish = [(0, 0), (5, 5)]
        self.checkpoints = [(0, 5), (2, 4)]
        self.assertEqual(algorithm(self.G, start_finish[0], start_finish[1], self.checkpoints), [(0, 0), (1, 1), (2, 2), (2, 3), (2, 4), (1, 5), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)])

    def test_same_start_finish(self):
        start_finish = [(0, 0), (0, 0)]
        self.checkpoints = [(0, 5)]
        self.assertEqual(algorithm(self.G, start_finish[0], start_finish[1], self.checkpoints), [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 4), (0, 3), (0, 2), (0, 1), (0, 0)])

    def test_no_path_to_checkpoint(self):
        start_finish = [(1, 1), (5, 5)]
        self.checkpoints = [(0, 0), (2, 4)]
        self.G.remove_edge((0, 0), (1, 0))
        self.G.remove_edge((0, 0), (0, 1))
        self.G.remove_edge((0, 0), (1, 1))
        self.assertEqual(algorithm(self.G, start_finish[0], start_finish[1], self.checkpoints), [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])

    def test_no_path_to_finish(self):
        start_finish = [(5, 5), (0, 0)]
        self.checkpoints = [(1, 1), (2, 4)]
        self.G.remove_edge((0, 0), (1, 0))
        self.G.remove_edge((0, 0), (0, 1))
        self.G.remove_edge((0, 0), (1, 1))
        self.assertEqual(algorithm(self.G, start_finish[0], start_finish[1], self.checkpoints), [])


if __name__ == "__main__":
    unittest.main()
