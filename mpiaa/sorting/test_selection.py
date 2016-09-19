from mpiaa.sorting.sortings import selection_sort
from mpiaa.sorting.sort_tests import SortTests
import unittest


class SelectionSortTests(SortTests):
    def setUp(self):
        self.set_sort_func(selection_sort)


if __name__ == "__main__":
    unittest.main()


