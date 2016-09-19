from mpiaa.sorting.sortings import bubble_sort
from mpiaa.sorting.sort_tests import SortTests
import unittest


class BubbleSortTests(SortTests):
    def setUp(self):
        self.set_sort_func(bubble_sort)


if __name__ == "__main__":
    unittest.main()


