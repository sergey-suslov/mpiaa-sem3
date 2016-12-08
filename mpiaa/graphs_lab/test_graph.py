from mpiaa.graphs_lab import StrongConnectivity
from mpiaa.graphs_lab.graph import Graph
import unittest


class GraphTests(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_empty(self):
        self.assertEqual(self.graph.get_vertices(), [])

    def test_add_edge(self):
        self.graph.add_edge("A", "B")
        self.assertEqual(len(self.graph.get_vertices()), 2)
        self.assertTrue(self.graph.has_edge("A", "B"))
        self.assertIn("B", self.graph.get_adjacent("A"))

    def test_add_edges(self):
        self.graph.add_edge("A", "B")
        self.graph.add_edge("A", "C")
        self.graph.add_vertex("D")
        self.assertEqual(len(self.graph.get_vertices()), 4)
        self.assertIn("C", self.graph.get_adjacent("A"))
        self.assertNotIn("D", self.graph.get_adjacent("A"))
        self.assertFalse(self.graph.has_edge("A", "D"))

    def test_weight(self):
        self.graph.add_edge("1", "2", 3)
        self.graph.add_edge("1", "3", 5)
        self.graph.add_edge("1", "4", 1)
        self.graph.add_edge("2", "1", 3)
        self.graph.add_edge("2", "3", 11)
        self.graph.add_edge("2", "4", 8)
        self.graph.add_edge("3", "2", 11)
        self.graph.add_edge("3", "1", 5)
        self.graph.add_edge("3", "6", 12)
        self.graph.add_edge("4", "2", 8)
        self.graph.add_edge("4", "1", 1)
        self.graph.add_edge("4", "7", 2)
        self.graph.add_edge("4", "10", 6)
        self.graph.add_edge("5", "6", 13)
        self.graph.add_edge("5", "7", 10)
        self.graph.add_edge("5", "10", 16)
        self.graph.add_edge("5", "8", 14)
        self.graph.add_edge("6", "10", 9)
        self.graph.add_edge("6", "3", 12)
        self.graph.add_edge("6", "5", 13)
        self.graph.add_edge("7", "4", 2)
        self.graph.add_edge("7", "8", 7)
        self.graph.add_edge("7", "5", 10)
        self.graph.add_edge("7", "9", 3)
        self.graph.add_edge("8", "5", 14)
        self.graph.add_edge("8", "7", 7)
        self.graph.add_edge("8", "9", 15)
        self.graph.add_edge("9", "8", 15)
        self.graph.add_edge("9", "7", 3)
        self.graph.add_edge("10", "4", 6)
        self.graph.add_edge("10", "5", 16)
        self.graph.add_edge("10", "6", 9)
        self.assertEqual(self.graph.get_ostov_minimal_weight(), 46)

    def test_strongly_connected_components(self):
        self.graph.add_edge("a", "b", 3)
        self.graph.add_edge("b", "e", 3)
        self.graph.add_edge("e", "a", 3)
        self.graph.add_edge("e", "f", 3)
        self.graph.add_edge("f", "g", 3)
        self.graph.add_edge("g", "f", 3)
        self.graph.add_edge("b", "f", 3)
        self.graph.add_edge("b", "c", 3)
        self.graph.add_edge("c", "g", 3)
        self.graph.add_edge("c", "d", 3)
        self.graph.add_edge("d", "h", 3)
        self.graph.add_edge("d", "c", 3)
        self.graph.add_edge("h", "g", 3)
        self.graph.add_edge("h", "d", 3)
        self.graph_dict = self.graph.adjacent
        a = self.graph.kosaraju()
        #self.assertEqual(StrongConnectivity.Condensation(self.graph_dict), [["a", "b", "e"], ["f", "g"], ["c", "d", "h"]])
        self.assertEqual(sorted([sorted(lst) for lst in self.graph.kosaraju()]),
                         sorted([sorted(lst) for lst in [["a", "b", "e"], ["f", "g"], ["c", "d", "h"]]]))

if __name__ == "__main__":
    unittest.main()
