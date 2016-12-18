from mpiaa.search.bstree import BSTree
from mpiaa.timer import time_us
from mpiaa.util import shuffled_ints, random_ints, powers_of


def linear_search(items, items_to_find):
    count = 0
    for item_to_find in items_to_find:
        if item_to_find in items:
            count += 1
    return count


def binary_search(items, items_to_find):
    tree = BSTree()
    for item in items:
        tree.insert(item)
    count = 0
    for item_to_find in items_to_find:
        if tree.find(item_to_find) is not None:
            count += 1
    return count


def all_unique(l):
    tree = BSTree()
    for i in l:
        if tree.find(i):
            return False
        else:
            tree.insert(i)
    return True

if __name__ == "__main__":
    time_us({
        "Lin. search": lambda args: linear_search(*args),
        "Bin. search": lambda args: binary_search(*args),
    }, ns=powers_of(10, 0, 5), generator=lambda n: (shuffled_ints(n), random_ints(1000)), repeats=10)
