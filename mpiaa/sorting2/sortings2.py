from random import randint

from mpiaa.sorting.sortings import merge_sort
from mpiaa.util import seq_ints, random_ints, random_int_pairs, powers_of
from mpiaa.timer import time_us

lst1 = [randint(1,21) for number in range(20)]
def less_than(a, b):
    return a < b or a == b

def counting_sort(lst, key):
    """In this algorithm, the final list is populated with zeroes;
    the number of elements less than or equal to each element in the list is
    counted by comparing the element (stored in a temporary list)
    with each other element in the list (taking its own occurence into account);
    the element is then placed in the final list, and
    using the number of occurences of said element, its duplicates
    are placed in the consecutive positions before its own in the final list."""

    final_lst = []
    for num in range(len(lst)):
        final_lst.append(0)

    for i in range(len(lst)):
        store_lst, count, counter = [lst[i]], 0, lst.count(lst[i])
        for j in range(len(lst)):
            if less_than(lst[j], store_lst[0]):
                count = count + 1
            else:
                count = count
        if counter > 1:
            for k in range(counter):
                final_lst[(count - 1) - k] = store_lst[0]
        else:
            final_lst[count - 1] = store_lst[0]
        store_lst.pop(0)
    return final_lst


def bucket_sort(items, get_key=lambda item: item):
    """
    Bucket sort

    :param items: list of items to sort
    :param get_key: function f(item) which returns item's key
    :return: sorted list of items
    """

    # Replace value by correct one
    num_of_buckets = 123

    # Replace function body by correct one
    def key_to_bucket(key):
        return key

    buckets = [[]]*num_of_buckets
    for item in items:
        buckets[key_to_bucket(get_key(item))].append(item)

    result = []

    # Rest of your code here

    return result


lst2 = [randint(100,999) for number in range(10)]

def radix_sort(lst, get_keys=(lambda item: item[0], lambda item: item[1])):
    lst3 = [str(x) for x in lst]
    temp = merge_sort([x[2]+x[1]+x[0] for x in lst3])
    temp1 = merge_sort([x[1]+x[0]+x[2] for x in temp])
    temp2 = merge_sort([x[2]+x[0]+x[1] for x in temp1])
    final_lst = [int(x) for x in temp2]
    return final_lst

if __name__ == "__main__":
    time_us({
        "Std sort": sorted,
        "Cnt. sort": counting_sort
        #,"Bucket sort": bucket_sort
    }, ns=powers_of(10, 0, 5), generator=lambda n: random_ints(n, -1000, 1000), repeats=100)

    time_us({
        "Std sort": sorted,
        "Radix sort": radix_sort
    }, ns=powers_of(10, 0, 5), generator=lambda n: random_int_pairs(n, -1000, 1000), repeats=100)

