import unittest
from mpiaa.sorting.sortings import all_unique


class SortTests(unittest.TestCase):

    def test_all_unique_false(self):
        self.assertFalse(all_unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 4]))

    def test_all_unique_true(self):
        self.assertTrue(all_unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


if __name__ == "__main__":
    unittest.main()
