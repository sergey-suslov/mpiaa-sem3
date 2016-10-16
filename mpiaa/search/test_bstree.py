from mpiaa.search.bstree import BSTree
import unittest


class BSTreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = BSTree()

    def test_insert(self):
        self.tree.insert(1)
        self.assertEqual(self.tree.find(1), 1)

    def test_find_in_empty(self):
        self.assertEqual(self.tree.find(1), None)

    def test_remove(self):
        self.tree.insert(1)
        self.tree.insert(2)
        self.tree.remove(1)
        self.assertEqual(self.tree.find(1), None)


if __name__ == "__main__":
    unittest.main()


