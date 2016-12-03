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
        self.assertTrue(self.graph.has_edge("B", "A"))
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
        self.graph.add_edge("A", "B", 3)
        self.graph.add_edge("A", "C", 2)
        self.graph.add_vertex("D")
        self.assertEqual(self.graph.get_weight("A"), {"B": 3, "C": 2})


if __name__ == "__main__":
    unittest.main()
