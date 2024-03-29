from mpiaa.search.bstree import BSTree
from mpiaa.search.search import all_unique
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

    def test_all_unique_false(self):
        self.assertFalse(all_unique([1, 2, 3, 1, 4]))

    def test_all_unique_true(self):
        self.assertTrue(all_unique([1, 2, 3, 5, 4]))
    #
    # def test_all_unique_true(self):
    #     self.tree.insert(1)
    #     self.tree.insert(2)
    #     self.tree.insert(3)
    #     self.tree.insert(4)
    #     self.tree.insert(5)
    #     self.assertTrue(self.tree.all_unique())

    def test_insert_strings(self):
        self.tree.insert("abc", 1)
        self.tree.insert("def", 2)
        self.assertEqual(self.tree.find(2), "def")

    def test_remove(self):
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
        self.tree.insert(2)
        self.assertEqual(self.tree.find(2), 2)

    def test_size_empty(self):
        self.assertEqual(self.tree.size(), 0)

    def test_size_dupes(self):
        self.tree.insert(2)
        self.assertEqual(self.tree.find(2), 2)

    def test_insert_replace_strings(self):
        self.tree.insert("abc", 1)
        self.tree.insert("cda", 1)
        self.tree.insert("efg", 2)
        self.assertEqual(self.tree.find(1), "cda")

    def test_height_single(self):
        self.tree.insert(1)
        self.assertEqual(self.tree.height(), 1)

    def test_height_balanced(self):
        self.tree.insert(2)
        self.tree.insert(1)
        self.tree.insert(3)
        self.assertEqual(self.tree.height(), 2)

    def test_height_unbalanced(self):
        self.tree.insert(1)
        self.tree.insert(2)
        self.tree.insert(3)
        self.assertEqual(self.tree.height(), 3)


if __name__ == "__main__":
    unittest.main()


