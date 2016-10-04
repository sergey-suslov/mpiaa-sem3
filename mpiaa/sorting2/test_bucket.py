import unittest

from mpiaa.sorting.sort_tests import SortTests
from mpiaa.sorting2.sortings2 import bucket_sort


class BucketSortTests(SortTests):
    def setUp(self):
        self.set_sort_func(bucket_sort)


if __name__ == "__main__":
    unittest.main()


