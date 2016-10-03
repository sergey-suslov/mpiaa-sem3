from mpiaa.sorting.sortings2 import radix_sort
from mpiaa.sorting.sort_tests import SortTests
import unittest


class RadixSortTests(SortTests):
    def setUp(self):
        self.set_sort_func(radix_sort)


if __name__ == "__main__":
    unittest.main()


