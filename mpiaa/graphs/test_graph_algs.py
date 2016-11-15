from mpiaa.graphs.graph import Graph
from mpiaa.graphs.graph_algs import is_connected, shortest_path, connected_components
import unittest


class GraphAlgsTests(unittest.TestCase):
    def setUp(self):
        self.graph1 = Graph(["a", "b", "c", "d"],
                            [("a", "b"), ("c", "d")])
        self.graph2 = Graph(["a", "b", "c", "d"],
                            [("a", "b"), ("b", "c"), ("c", "d"), ("d", "a")])
        self.graph3 = Graph(["a", "b", "c", "d", "e"],
                            [("a", "b"), ("a", "c"), ("a", "d")])
        self.graph4 = Graph(["a", "b", "c", "d", "e"],
                            [("a", "b"), ("b", "c"), ("a", "c"), ("c", "e"),
                             ("c", "d"), ("d", "e")])

    def test_is_connected(self):
        self.assertFalse(is_connected(self.graph1))
        self.assertTrue(is_connected(self.graph2))
        self.assertFalse(is_connected(self.graph3))
        self.assertTrue(is_connected(self.graph4))

    def test_shortest_path(self):
        self.assertEqual(shortest_path(self.graph1, "a", "d"), [])
        self.assertEqual(shortest_path(self.graph2, "a", "d"), ["a", "d"])
        self.assertEqual(shortest_path(self.graph3, "a", "e"), [])
        self.assertEqual(shortest_path(self.graph4, "a", "e"), ["a", "c", "e"])

    def assertListsOfListsEqual(self, ll1, ll2):
        s1 = set([set(l) for l in ll1])
        s2 = set([set(l) for l in ll2])
        self.assertEqual(s1, s2)

    def test_connected_components(self):
        self.assertListsOfListsEqual(connected_components(self.graph1), [["a", "b"], ["c", "d"]])
        self.assertListsOfListsEqual(connected_components(self.graph2), [["a", "b", "c", "d"]])
        self.assertListsOfListsEqual(connected_components(self.graph3), [["a", "b", "c", "d"], ["e"]])
        self.assertListsOfListsEqual(connected_components(self.graph4), [["a", "b", "c", "d", "e"]])


if __name__ == "__main__":
    unittest.main()
    