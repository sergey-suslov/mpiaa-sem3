from mpiaa.sorting.sortings import quick_sort
from mpiaa.sorting.sort_tests import SortTests
import unittest


class QuickSortTests(SortTests):
    def setUp(self):
        self.set_sort_func(quick_sort)


if __name__ == "__main__":
    unittest.main()


