import unittest


class SortTests(unittest.TestCase):
    def set_sort_func(self, func):
        self.sort_func = func

    def setUp(self):
        self.set_sort_func(sorted)

    def test_empty(self):
        self.assertEqual(self.sort_func([]), [])

    def test_single(self):
        self.assertEqual(self.sort_func([1]), [1])

    def test_multiple(self):
        self.assertEqual(self.sort_func([3, 2, 1]), [1, 2, 3])

    def test_multiple_no_sort(self):
        self.assertEqual(self.sort_func([1, 2, 3]), [1, 2, 3])

    def test_multiple_dupes(self):
        self.assertEqual(self.sort_func([3, 2, 0, 2, 5]), [0, 2, 2, 3, 5])


if __name__ == "__main__":
    unittest.main()


