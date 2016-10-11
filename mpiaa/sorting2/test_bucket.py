import unittest

from mpiaa.sorting.sort_tests import SortTests
from mpiaa.sorting2.sortings2 import bucket_sort


class BucketSortTests(SortTests):
    def setUp(self):
        self.set_sort_func(bucket_sort)
        self.pair_key = lambda el: el[1]

    def test_pairs_single(self):
        self.assertEqual(bucket_sort([("A", 1)], self.pair_key), [("A", 1)])

    def test_pairs_multiple(self):
        self.assertEqual(bucket_sort([("A", 1), ("B", 0), ("C", -1)], self.pair_key),
                         [("C", -1), ("B", 0), ("A", 1)])


if __name__ == "__main__":
    unittest.main()


