from mpiaa.intro.functions import find
from mpiaa.util import seq_ints
import unittest

class FindTests(unittest.TestCase):
    def test_empty(self):
        self.assertFalse(find([], 1))

    def test_single(self):
        self.assertTrue(find([1], 1))

    def test_multiple(self):
        self.assertTrue(find([1, 2, 3], 2))

    def test_big(self):
        self.assertTrue(find(seq_ints(10000), 5555))

    def test_single_fail(self):
        self.assertFalse(find([1], 2))

    def test_multiple_fail(self):
        self.assertFalse(find([1, 2, 3], 0))

    def test_big_fail(self):
        self.assertFalse(find(seq_ints(10000), 10000))


if __name__ == "__main__":
    unittest.main()


