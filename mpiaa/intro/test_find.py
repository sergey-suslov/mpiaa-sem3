from mpiaa.intro.functions import find
import unittest

class FindTests(unittest.TestCase):
    def test_empty(self):
        self.assertFalse(find([], 1))

    def test_single(self):
        self.assertTrue(find([1], 1))

    def test_multiple(self):
        self.assertTrue(find([1, 2, 3], 2))

    def test_single_not_found(self):
        self.assertFalse(find([1], 2))

    def test_multiple_not_found(self):
        self.assertFalse(find([1, 2, 3], 0))


if __name__ == "__main__":
    unittest.main()


