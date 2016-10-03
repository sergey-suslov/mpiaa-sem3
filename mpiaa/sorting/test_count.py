from mpiaa.sorting.sortings2 import count_sort
from mpiaa.sorting.sort_tests import SortTests
import unittest


class CountSortTests(SortTests):
    def setUp(self):
        self.set_sort_func(count_sort)


if __name__ == "__main__":
    unittest.main()


