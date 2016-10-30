from mpiaa.search2.hash_table import HashTable
import unittest


class HashTableTests(unittest.TestCase):
    def setUp(self):
        self.int_hash_table = HashTable(100, lambda key: key)
        self.str_hash_table = HashTable(100, lambda key: hash(key))

    def test_int_find_in_empty(self):
        self.assertIsNone(self.int_hash_table.find(1))

    def test_str_find_in_empty(self):
        self.assertIsNone(self.str_hash_table.find("abc"))

    def test_int_insert(self):
        self.int_hash_table.insert("a", 1)
        self.assertEqual(self.int_hash_table.find(1), "a")

    def test_int_insert_mod(self):
        self.int_hash_table.insert("a", 1)
        self.int_hash_table.insert("b", 101)
        self.int_hash_table.insert("c", 201)
        self.assertEqual(self.int_hash_table.find(101), "b")

    def test_str_insert(self):
        self.str_hash_table.insert("a", "abc")
        self.assertEqual(self.str_hash_table.find("abc"), "a")

    def test_int_insert_dupes(self):
        self.int_hash_table.insert("a", 1)
        self.int_hash_table.insert("b", 2)
        self.int_hash_table.insert("c", 1)
        self.int_hash_table.insert("a", 3)
        self.assertEqual(self.int_hash_table.find(1), "c")

    def test_str_insert_dupes(self):
        self.str_hash_table.insert("a", "abc")
        self.str_hash_table.insert("b", "efg")
        self.str_hash_table.insert("a", "klm")
        self.str_hash_table.insert("c", "abc")
        self.assertEqual(self.str_hash_table.find("abc"), "c")

    def test_int_remove(self):
        self.int_hash_table.insert("a", 1)
        self.int_hash_table.insert("b", 2)
        self.int_hash_table.remove(2)
        self.assertIsNone(self.int_hash_table.find(2))

    def test_str_remove(self):
        self.str_hash_table.insert("a", "abc")
        self.str_hash_table.insert("b", "cba")
        self.str_hash_table.remove("cba")
        self.assertIsNone(self.str_hash_table.find("cba"))

    def test_size_empty(self):
        self.assertEqual(self.int_hash_table.size(), 0)

    def test_size(self):
        self.int_hash_table.insert("a", 1)
        self.assertEqual(self.int_hash_table.size(), 1)

    def test_size_dupes(self):
        self.int_hash_table.insert("a", 1)
        self.int_hash_table.insert("a", 2)
        self.int_hash_table.insert("c", 1)
        self.assertEqual(self.int_hash_table.size(), 2)

    def test_size_mod(self):
        self.int_hash_table.insert("a", 1)
        self.int_hash_table.insert("b", 101)
        self.int_hash_table.insert("c", 201)
        self.assertEqual(self.int_hash_table.size(), 3)


if __name__ == "__main__":
    unittest.main()


