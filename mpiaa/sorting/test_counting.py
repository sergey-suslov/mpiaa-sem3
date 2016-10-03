from mpiaa.sorting.sortings2 import counting_sort
from mpiaa.sorting.sort_tests import SortTests
import unittest


class CountSortTests(SortTests):
    def setUp(self):
        self.set_sort_func(counting_sort)


if __name__ == "__main__":
    unittest.main()


