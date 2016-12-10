from mpiaa.np.max_clique import is_clique
from mpiaa.graphs.graph import Graph
import unittest


class IsCliqueTests(unittest.TestCase):
    def setUp(self):
        self.graph = Graph(["a", "b", "c", "d"],
                           [("a", "b"), ("a", "c"), ("b", "c"), ("a", "d")])

    def test_empty(self):
        self.assertFalse(is_clique(self.graph, []))

    def test_single(self):
        self.assertTrue(is_clique(self.graph, ["a"]))

    def test_double(self):
        self.assertTrue(is_clique(self.graph, ["a", "b"]))

    def test_double_false(self):
        self.assertFalse(is_clique(self.graph, ["b", "d"]))

    def test_multiple(self):
        self.assertTrue(is_clique(self.graph, ["a", "b", "c"]))

    def test_multiple_false(self):
        self.assertFalse(is_clique(self.graph, ["a", "b", "c", "d"]))


if __name__ == "__main__":
    unittest.main()
