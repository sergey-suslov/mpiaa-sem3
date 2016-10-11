import unittest

from mpiaa.sorting.sort_tests import SortTests
from mpiaa.sorting2.sortings2 import counting_sort


class CountSortTests(SortTests):
    def setUp(self):
        self.set_sort_func(counting_sort)
        self.pair_key = lambda el: el[1]

    def test_pairs_single(self):
        self.assertEqual(counting_sort([("A", 1)], self.pair_key), [("A", 1)])

    def test_pairs_multiple(self):
        self.assertEqual(counting_sort([("A", 1), ("B", 0), ("C", -1)], self.pair_key),
                         [("C", -1), ("B", 0), ("A", 1)])


if __name__ == "__main__":
    unittest.main()


