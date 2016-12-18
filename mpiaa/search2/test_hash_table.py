from mpiaa.search2.Human import Human
from mpiaa.search2.hash_table import HashTable
from mpiaa.search2.search2 import all_unique
import unittest


class HashTableTests(unittest.TestCase):
    people = "Edythe Bourret 30 Jan 1955\nAlena Jerdon 31 Aug 1914\nBrooks Dalleva 6 May 1946\nArmandina Tippey 13 Feb 1922\nNeoma Lamey 1 Dec 1983\nLourdes Brooms 2 Feb 1903\nAdrianne Osika 9 Apr 1928\nStephaine Ehrke 8 Sept 1985\nHelaine Govern 3 Oct 1960\nSheena Knall 2 Nov 1965\nAngie Hurless 22 July 1989\nAngelica Zumbrennen 4 May 1933\nBernardine Dearman 20 Apr 1939\nKacie Sagraves 24 Aug 1994\nTequila Odonahue 7 June 1940\nAlita Radell 27 Jan 1996\nShannon Lardin 8 July 1924\nAkiko Greengo 1 Apr 1939\nCorine Corrick 6 Mar 1949\nBernarda Iqbal 1 Feb 1906\nDorine Muzzillo 8 Apr 1947\nMaurice Rosenthal 30 Jan 1995"
    peoples = people.split("\n")
    peoples = [p.split(' ') for p in peoples]
    human = [Human(p[0], p[1], p[2], p[3], p[4]) for p in peoples]

    def setUp(self):
        self.str_hash_table = HashTable(len(self.human), lambda key: hash(key) % len(self.human))

    def test_all_unique_true(self):
        self.assertTrue(all_unique([1, 2, 3, 4, 5, 6, 0]))

    def test_all_unique_false(self):
        self.assertFalse(all_unique([1, 2, 3, 2, 5, 6, 0]))

    def test_remove(self):
        self.str_hash_table.insert(1, 1)
        self.str_hash_table.insert(1, 2)
        self.str_hash_table.insert(2, 2)
        self.str_hash_table.insert(3, 3)
        self.str_hash_table.insert(4, 4)
        self.str_hash_table.insert(5, 5)
        self.str_hash_table.remove(2)
        self.assertEqual(self.str_hash_table.find(2), None)
        self.assertEqual(self.str_hash_table.get_size(), 5)

    def test_str_find_in_empty(self):
        self.assertIsNone(self.str_hash_table.find("abc"))

    def test_str_insert_find(self):
        for i in range(7):
            self.str_hash_table.insert(self.human[i], self.human[i].last_name+self.human[i].day)
        self.assertEqual(self.str_hash_table.find(self.human[0].last_name+self.human[0].day), [['Bourret30', self.human[0]]])

    def test_str_find_tuples(self):
        people = "Edythe Bourret 30 Jan 1955\nAlena Jerdon 31 Aug 1914\nBrooks Dalleva 6 May 1946\nArmandina Tippey 13 Feb 1922\nNeoma Lamey 1 Dec 1983\nLourdes Brooms 2 Feb 1903\nAdrianne Osika 9 Apr 1928\nStephaine Ehrke 8 Sept 1985\nHelaine Govern 3 Oct 1960\nSheena Knall 2 Nov 1965\nAngie Hurless 22 July 1989\nAngelica Zumbrennen 4 May 1933\nBernardine Dearman 20 Apr 1939\nKacie Sagraves 24 Aug 1994\nTequila Odonahue 7 June 1940\nAlita Radell 27 Jan 1996\nShannon Lardin 8 July 1924\nAkiko Greengo 1 Apr 1939\nCorine Corrick 6 Mar 1949\nBernarda Iqbal 1 Feb 1906\nDorine Muzzillo 8 Apr 1947\nMaurice Rosenthal 30 Jan 1995"
        peoples = people.split("\n")
        peoples = [p.split(' ') for p in peoples]
        human = [Human(p[0], p[1], p[2], p[3], p[4]) for p in peoples]
        for i in range(7):
            self.str_hash_table.insert(self.human[i], self.human[i].last_name+self.human[i].day)
        self.assertEqual(self.str_hash_table.find(self.human[2].last_name+self.human[2].day), [['Dalleva6', self.human[2]]])

if __name__ == "__main__":
    unittest.main()


