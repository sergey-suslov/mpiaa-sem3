from mpiaa.search2.hash_table import HashTable
from mpiaa.timer import time_us
from mpiaa.util import shuffled_ints, random_ints, powers_of, random_strings


def linear_search(items, items_to_find):
    count = 0
    for item_to_find in items_to_find:
        if item_to_find in items:
            count += 1
    return count


def hash_search(hash_table_size, hash_func, items, items_to_find):
    hash_table = HashTable(hash_table_size, hash_func)
    for item in items:
        hash_table.insert(item, item)
    count = 0
    for item_to_find in items_to_find:
        if hash_table.find(item_to_find) is not None:
            count += 1
    return count


def to_string_list(items):
    return [str(item) for item in items]


if __name__ == "__main__":
    print("Integer keys")
    time_us({
        "Lin. search": lambda args: linear_search(*args),
        "Hash search": lambda args: hash_search(100, lambda x: x % 100, *args),
    }, ns=powers_of(10, 0, 5), generator=lambda n: (shuffled_ints(n), random_ints(1000)), repeats=10)

    print("String keys")
    time_us({
        "Lin. search": lambda args: linear_search(*args),
        "Hash search": lambda args: hash_search(100, lambda x: len(x) % 100, *args),
    }, ns=powers_of(10, 0, 5), generator=lambda n: (random_strings(n, 3), random_strings(1000, 3)), repeats=10)
