from mpiaa.intro.functions import all_unique
from mpiaa.util import seq_ints
import unittest

class AllUniqueTests(unittest.TestCase):
    def test_empty(self):
        self.assertFalse(all_unique([]))

    def test_single(self):
        self.assertTrue(all_unique([1]))

    def test_multiple(self):
        self.assertTrue(all_unique([1, 2, 3]))

    def test_big(self):
        self.assertTrue(all_unique(seq_ints(10000)))

    def test_multiple_fail(self):
        self.assertFalse(all_unique([1, 2, 3, 2]))

    def test_big_fail(self):
        self.assertFalse(all_unique(seq_ints(10000) + [0]))


if __name__ == "__main__":
    unittest.main()


