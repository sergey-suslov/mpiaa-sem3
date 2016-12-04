from mpiaa.graphs_lab.graph import Graph
from mpiaa.graphs_lab.graph_algs import is_connected, shortest_path, connected_components
import unittest


class GraphAlgsTests(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()



    def test_shortest_path(self):
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
        print(shortest_path(self.graph, "1"))
        self.sorted_answer = {'7': '4', '9': '7', '2': '1', '6': '10', '4': '1', '3': '1', '10': '4', '5': '7', '8': '7',
                          '1': None}
        self.sorted_result = shortest_path(self.graph, "1")[1]
        sorted(self.sorted_answer, key=lambda x: list(x)[0])
        sorted(self.sorted_result, key=lambda x: list(x)[0])
        self.assertEqual(self.sorted_result, self.sorted_answer)
        # self.assertEqual(shortest_path(self.graph2, "a", "d")[1], ["a", "d"])
        # self.assertEqual(shortest_path(self.graph3, "a", "e")[1], [])
        # self.assertEqual(shortest_path(self.graph4, "a", "e")[1], ["a", "c", "e"])

    # def assertListsOfListsEqual(self, ll1, ll2):
    #     s1 = sorted([sorted(l) for l in ll1])
    #     s2 = sorted([sorted(l) for l in ll2])
    #     self.assertEqual(s1, s2)
    #
    # def test_connected_components(self):
    #     self.assertListsOfListsEqual(connected_components(self.graph1), [["a", "b"], ["c", "d"]])
    #     self.assertListsOfListsEqual(connected_components(self.graph2), [["a", "b", "c", "d"]])
    #     self.assertListsOfListsEqual(connected_components(self.graph3), [["a", "b", "c", "d"], ["e"]])
    #     self.assertListsOfListsEqual(connected_components(self.graph4), [["a", "b", "c", "d", "e"]])


if __name__ == "__main__":
    unittest.main()
