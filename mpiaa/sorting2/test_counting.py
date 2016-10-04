import unittest

from mpiaa.sorting.sort_tests import SortTests
from mpiaa.sorting2.sortings2 import counting_sort


class CountSortTests(SortTests):
    def setUp(self):
        self.set_sort_func(counting_sort)


if __name__ == "__main__":
    unittest.main()


