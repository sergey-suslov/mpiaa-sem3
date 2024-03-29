import time

from mpiaa.search2.Human import Human
from mpiaa.search2.hash_table import HashTable

if __name__ == "__main__":
    people = open("../../record_gen/records_1e4.txt", "r").read()
    peoples = people.split("\n")
    peoples = [p.split(' ') for p in peoples]
    humen = [Human(p[0], p[1], p[2], p[3], p[4]) for p in peoples]

    str_hash_table = HashTable(num_of_buckets=len(humen), hash_func= lambda key: hash(key))
    for i in humen:
        str_hash_table.insert(i, str(i.last_name) + str(i.age))
    for i in str_hash_table.buckets:
        if i:
            pass
            #print(i[0])
        else:
            pass
            #print("None")
    k = 2
    indexes = [n for n in range(len(humen)) if n % k == 0]
    t1 = time.time()

    for i in indexes:
        str_hash_table.find(str(humen[i].last_name) + str(humen[i].age))

    t2 = time.time()

    print("Search every " + str(k) + " element, time: " + str(t2-t1))

    linear_list = []

    for i in humen:
        linear_list.append(str(i.first_name) + str(i.age))

    t1 = time.time()
    for i in indexes:
        if str(humen[i].last_name) + str(humen[i].age) in linear_list:
            pass
    t2 = time.time()
    print("Search every " + str(k) + " element, linear list time: " + str(t2 - t1))

    len_max = 0
    summary_len = 0
    count = 0

    for i in str_hash_table.buckets:
        if i:
            length = len(i)
            summary_len += length
            count += 1
            if length > len_max:
                len_max = length


    print("Max len:  " + str(len_max))
    print("Elements aren't unique" if len_max > 1 else "All elements are unique")
    print("Average len:  " + str(int(count) / str_hash_table.num_of_el))
    print("Fullness: " + str(count / str_hash_table.size))

