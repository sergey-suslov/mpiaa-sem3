from mpiaa.sorting.sortings import merge_sort
from mpiaa.sorting.sort_tests import SortTests
import unittest


class MergeSortTests(SortTests):
    def setUp(self):
        self.set_sort_func(merge_sort)


if __name__ == "__main__":
    unittest.main()


