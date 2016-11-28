from mpiaa.np.max_clique import all_combinations
import unittest


class AllCombinationsTests(unittest.TestCase):
    def assertCombEqual(self, lst1, lst2):
        s1 = frozenset([frozenset(l) for l in lst1])
        s2 = frozenset([frozenset(l) for l in lst2])
        self.assertEqual(s1, s2)

    def test_empty(self):
        self.assertCombEqual(all_combinations([]), [])

    def test_single(self):
        self.assertCombEqual(all_combinations(["a"]), [["a"]])

    def test_double(self):
        self.assertCombEqual(all_combinations(["a", "b"]), [["a"], ["b"], ["a", "b"]])

    def test_multiple(self):
        self.assertCombEqual(all_combinations(["a", "b", "c"]),
                             [["a"], ["b"], ["c"], ["a", "b"], ["a", "c"], ["b", "c"], ["a", "b", "c"]])


if __name__ == "__main__":
    unittest.main()
