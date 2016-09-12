from mpiaa.intro.functions import all_unique
import unittest

class AllUniqueTests(unittest.TestCase):
    def test_empty(self):
        self.assertFalse(all_unique([]))

    def test_single(self):
        self.assertTrue(all_unique([1]))

    def test_multiple(self):
        self.assertTrue(all_unique([1, 2, 3]))

    def test_multiple_not_unique(self):
        self.assertFalse(all_unique([1, 2, 3, 2]))


if __name__ == "__main__":
    unittest.main()


