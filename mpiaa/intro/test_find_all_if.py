from mpiaa.intro.functions import find_all_if
import unittest

class FindAllIfTests(unittest.TestCase):
    def setUp(self):
        self.is_positive = lambda x: x > 0

    def test_empty(self):
        self.assertEqual(find_all_if([], self.is_positive), [])

    def test_single(self):
        self.assertEqual(find_all_if([1], self.is_positive), [1])

    def test_multiple(self):
        self.assertEqual(find_all_if([1, -2, 3], self.is_positive), [1, 3])

    def test_single_not_found(self):
        self.assertEqual(find_all_if([-1], self.is_positive), [])

    def test_multiple_not_found(self):
        self.assertEqual(find_all_if([-1, -2, -3], self.is_positive), [])


if __name__ == "__main__":
    unittest.main()


