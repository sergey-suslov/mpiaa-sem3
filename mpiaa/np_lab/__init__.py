import random

import time

from mpiaa.np_lab import max_clique
from mpiaa.np_lab import funcs
from mpiaa.np_lab.item import Item
from mpiaa.np_lab.Backpack import Backpack

def default(list, bp):
    list_of_items = list
    max_item = max(list_of_items, key=lambda item: item.price_cooficient)
    while list_of_items:
        bp.insert(max_item)
        del list_of_items[list_of_items.index(max_item)]
        if list_of_items:
            max_item = max(list_of_items, key=lambda item: item.price_cooficient)
    return bp.current_weight, bp.full_price

def greedy_algorithm(list, bp):
    list_of_items = list
    list_of_items.sort(key=lambda item: item.price_cooficient)
    list_of_items.reverse()
    for i in list_of_items:
        bp.insert(i)
    return bp.current_weight, bp.full_price

if __name__ == "__main__":
    list_of_items = [Item("item " + str(i), random.random() * 100, random.random() * 1000, i) for i in range(200)]
    static_list = list_of_items[:]
    bp = Backpack(350)
    t1 = time.time()
    print(default(list_of_items, bp))
    t2 = time.time()
    print("default algorythm time: " + str(t2 - t1))
    bp = Backpack(350)
    bp.full_price = 0
    bp.items = []
    #greedy
    t1 = time.time()
    print(greedy_algorithm(static_list, bp))
    t2 = time.time()
    print("greedy algorythm time: " + str(t2 - t1))

