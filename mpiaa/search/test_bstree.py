from mpiaa.search.bstree import BSTree
import unittest


class BSTreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = BSTree()

    def test_find_in_empty(self):
        self.assertIsNone(self.tree.find(1))

    def test_insert(self):
        self.tree.insert(1)
        self.assertEqual(self.tree.find(1), 1)

    def test_insert_complex(self):
        self.tree.insert(2)
        self.tree.insert(1)
        self.tree.insert(5)
        self.assertEqual(self.tree.find(5), 5)

    def test_insert_strings(self):
        self.tree.insert("abc", 1)
        self.tree.insert("def", 2)
        self.assertEqual(self.tree.find(2), "def")

    def test_remove(self):
        self.tree.insert(1)
        self.tree.insert(2)
        self.tree.remove(1)
        self.assertIsNone(self.tree.find(1))

    def test_remove_complex(self):
        self.tree.insert(3)
        self.tree.insert(2)
        self.tree.insert(5)
        self.tree.insert(4)
        self.tree.insert(6)
        self.tree.remove(3)
        self.assertIsNone(self.tree.find(3))

    def test_size(self):
        self.tree.insert(3)
        self.tree.insert(1)
        self.tree.insert(2)
        self.assertEqual(self.tree.size(), 3)

    def test_size_empty(self):
        self.assertEqual(self.tree.size(), 0)

    def test_size_dupes(self):
        self.tree.insert(1)
        self.tree.insert(2)
        self.tree.insert(2)
        self.assertEqual(self.tree.size(), 2)

    def test_insert_replace_strings(self):
        self.tree.insert("abc", 1)
        self.tree.insert("cda", 1)
        self.tree.insert("efg", 2)
        self.assertEqual(self.tree.find(1), "cda")


if __name__ == "__main__":
    unittest.main()


