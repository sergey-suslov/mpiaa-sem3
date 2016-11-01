class HashTable(object):
    def __init__(self, num_of_buckets, hash_func):
        """
        Hash table constructor.

        :param num_of_buckets: number of buckets in the hash table
        :param hash_func: f(key), for each key must return integer in [0, num_of_buckets)
        """
        self.buckets = []
        for i in range(num_of_buckets):
            self.buckets.append([])
        self.hash_func = hash_func

    def insert(self, item, key):
        """
        Inserts item in the hash table with given key.
        If key already exists, replaces old item with the new one.

        :param item: item(object) to insert
        :param key: item's key
        """
        # Replace by correct code
        pass

    def find(self, key):
        """
        Returns item for the given key or None if key doesn't exist.

        :param key: key of an item to find
        :return: item or None
        """
        # Replace by correct code
        return None

    def remove(self, key):
        """
        Removes item (and its key) for the given key from the hash table.

        :param key: key of an item to remove
        """
        # Replace by correct code
        pass

    def size(self):
        """
        Returns number of items in the hash table.

        :return: number of items
        """
        # Replace by correct code
        return 0
