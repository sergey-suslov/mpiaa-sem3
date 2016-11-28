from mpiaa.np.max_clique import max_clique
from mpiaa.graphs.graph import Graph
import unittest


class MaxCliqueTests(unittest.TestCase):
    def setUp(self):
        self.graph1 = Graph()
        self.graph2 = Graph(["a", "b", "c", "d"],
                            [("a", "b"), ("a", "c"), ("b", "c"), ("a", "d")])
        self.graph3 = Graph(["a", "b"])
        self.graph4 = Graph(["a", "b", "c"], [("a", "b"), ("b", "c")])

    def assertCliqueEqual(self, l1, l2):
        self.assertEqual(frozenset(l1), frozenset(l2))

    def assertCliqueIn(self, l1, l2):
        cliques = [frozenset(elem) for elem in l2]
        self.assertIn(frozenset(l1), cliques)

    def test_empty(self):
        self.assertCliqueEqual(max_clique(self.graph1), [])

    def test_multiple(self):
        self.assertCliqueEqual(max_clique(self.graph2), ["a", "b", "c"])

    def test_single(self):
        self.assertCliqueIn(max_clique(self.graph3), [["a"], ["b"]])

    def test_double(self):
        self.assertCliqueIn(max_clique(self.graph4), [["a", "b"], ["b", "c"]])


if __name__ == "__main__":
    unittest.main()
