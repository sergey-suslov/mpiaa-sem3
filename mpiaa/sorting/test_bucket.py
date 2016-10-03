from mpiaa.sorting.sortings2 import bucket_sort
from mpiaa.sorting.sort_tests import SortTests
import unittest


class BucketSortTests(SortTests):
    def setUp(self):
        self.set_sort_func(bucket_sort)


if __name__ == "__main__":
    unittest.main()


