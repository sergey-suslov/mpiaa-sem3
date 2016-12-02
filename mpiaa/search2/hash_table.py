class HashTable(object):
    def custom_hash(self, key):
        return hash(key) % self.size

    def __init__(self, num_of_buckets, hash_func):
        self.buckets = []
        self.num_of_el = 0
        self.size = num_of_buckets*2
        for i in range(num_of_buckets*2):
            self.buckets.append([])
        self.hash_func = hash_func

    def append_last(self, search_from, key, item):
        while self.buckets[search_from]:
            if self.buckets[search_from][0][0] == key:
                self.buckets[search_from].append([key, item])
                return
            if self.size - 1 == search_from:
                search_from = 0
            else:
                search_from += 1
        self.buckets[search_from].append([key, item])
        self.num_of_el += 1

    def insert(self, item, key):
        if self.num_of_el < self.size:
            hash_key = self.custom_hash(key)
            if self.buckets[hash_key]:
                if self.buckets[hash_key][0][0] == key:
                    self.buckets[hash_key].append([key, item])
                else:
                    self.append_last(hash_key, key, item)
            else:
                self.buckets[hash_key].append([key, item,])
                self.num_of_el += 1

    def search_last(self, start, key):
        i = start
        while self.buckets[i] and self.buckets[i][0][0] != key:
            if i == self.size - 1:
                i = 0
            else:
                i += 1
            if i == start:
                return None
        return self.buckets[i]

    def find(self, key):
        hash_key = self.custom_hash(key)
        if self.buckets[hash_key]:
            if self.buckets[hash_key][0][0] == key:
                return self.buckets[hash_key]
            else:
                return self.search_last(hash_key, key)
        else:
            return None
