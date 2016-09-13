from mpiaa.intro.functions import find_if
import unittest

class FindIfTests(unittest.TestCase):
    def setUp(self):
        self.is_positive = lambda x: x > 0

    def test_empty(self):
        self.assertEqual(find_if([], self.is_positive), None)

    def test_single(self):
        self.assertEqual(find_if([1], self.is_positive), 1)

    def test_multiple(self):
        self.assertEqual(find_if([-1, 2, -3], self.is_positive), 2)

    def test_multiple_return_first(self):
        self.assertEqual(find_if([-1, 2, 3, -3], self.is_positive), 2)

    def test_single_not_found(self):
        self.assertEqual(find_if([-1], self.is_positive), None)

    def test_multiple_not_found(self):
        self.assertEqual(find_if([-1, -2, -3], self.is_positive), None)


if __name__ == "__main__":
    unittest.main()


