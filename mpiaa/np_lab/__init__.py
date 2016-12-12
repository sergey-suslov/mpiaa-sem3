import random

import time

from mpiaa.np_lab import max_clique
from mpiaa.np_lab import funcs
from mpiaa.np_lab.item import Item
from mpiaa.np_lab.Backpack import Backpack


def default(l, backpack):
    items = l
    max_item = max(items, key=lambda x: x.price_cooficient)
    while items:
        backpack.insert(max_item)
        del items[items.index(max_item)]
        if items:
            max_item = max(items, key=lambda x: x.price_cooficient)
    return backpack.current_weight, backpack.full_price


def greedy_algorithm(l, backpack):
    items = l
    items.sort(key=lambda x: x.price_cooficient, reverse=True)
    for i in items:
        backpack.insert(i)
    return backpack.current_weight, backpack.full_price

if __name__ == "__main__":
    list_of_items = [Item("item " + str(i), random.random() * 100, random.random() * 1000, i) for i in range(1000000)]
    static_list = list_of_items[:]
    bp = Backpack(3050)
    t1 = time.time()
    #print(default(list_of_items, bp))
    t2 = time.time()
    print("default algorythm time: " + str(t2 - t1))
    bp = Backpack(3050)
    bp.full_price = 0
    bp.items = []
    #greedy
    t1 = time.time()
    print(greedy_algorithm(static_list, bp))
    t2 = time.time()
    print("greedy algorythm time: " + str(t2 - t1))

