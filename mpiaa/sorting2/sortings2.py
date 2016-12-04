from math import floor, log10
from random import randint

from mpiaa.sorting.sortings import merge_sort
from mpiaa.util import seq_ints, random_ints, random_int_pairs, powers_of
from mpiaa.timer import time_us

lst1 = [randint(1,21) for number in range(20)]
def less_than(a, b, key):
    return key(a) < key(b) or key(a) == key(b)

def counting_sort(lst, get_key=lambda item: item):
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
            if less_than(lst[j], store_lst[0], key=get_key):
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


def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [alist[i*length // wanted_parts: (i+1)*length // wanted_parts]
             for i in range(wanted_parts)]


def bucket_sort(lst, get_key=lambda item: item):
    if not lst:
        return []
    if len(lst) == 1:
        return lst
    final_sort = lambda item: get_key(item[0])
    bucket, bucket1, bucket2 = [], [], []  # The three empty buckets
    max_value = max(lst, key=get_key)
    min_value = min(lst, key=get_key)
    value_range = ((get_key(max_value) - get_key(min_value))/2)
    # Populating the buckets with the list elements
    for i in range(len(lst)):
        if get_key(lst[i]) < floor(get_key(max_value) - value_range):
            bucket.append(lst[i])
        else:
            bucket1.append(lst[i])

    bucket.sort(key=get_key)
    bucket1.sort(key=get_key)

    # Prints the buckets and their contents
    # The actual sorting
    final_lst = bucket + bucket1
    print("Sorted list:", final_lst)
    return final_lst


def radix_sort(lst, get_keys=(lambda item: item[0], lambda item: item[1])):
    lst3 = [str(x) for x in lst]
    temp = merge_sort([x[1]+ x[2] + x[3] for x in lst3])
    temp1 = merge_sort([x[3] + x[2] + x[1] for x in temp])
    final_lst = [int(x) for x in temp1]
    return final_lst

if __name__ == "__main__":
    time_us({
        "Std sort": sorted,
        "Cnt. sort": counting_sort
        #,"Bucket sort": bucket_sort
    }, ns=powers_of(10, 0, 5), generator=lambda n: random_ints(n, -1000, 1000), repeats=100)
    #
    # time_us({
    #     "Std sort": sorted,
    #     "Radix sort": radix_sort
    # }, ns=powers_of(10, 0, 5), generator=lambda n: random_int_pairs(n, -1000, 1000), repeats=100)

