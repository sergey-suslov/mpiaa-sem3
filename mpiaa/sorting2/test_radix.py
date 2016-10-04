import unittest

from mpiaa.sorting2.sortings2 import radix_sort


class RadixSortTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(radix_sort([]), [])

    def test_single(self):
        self.assertEqual(radix_sort([(1, 1)]), [(1, 1)])

    def test_multiple(self):
        self.assertEqual(radix_sort([(2, 2), (1, 1), (1, 2)]), [(1, 1), (1, 2), (2, 2)])

    def test_multiple_no_sort(self):
        self.assertEqual(radix_sort([(1, 1), (1, 2), (2, 2)]), [(1, 1), (1, 2), (2, 2)])

    def test_multiple_dupes(self):
        self.assertEqual(radix_sort([(1, 2), (2, 2), (1, 1), (1, 2), (0, 0)]),
                         [(0, 0), (1, 1), (1, 2), (1, 2), (2, 2)])


if __name__ == "__main__":
    unittest.main()


