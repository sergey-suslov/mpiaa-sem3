from math import floor, log10
from random import randint

import math

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


def bucket_sort(array, get_key=lambda item: item, bucketSize=2):
    if len(array) == 0:
        return array

    # Determine minimum and maximum values
    minValue = min(array, key=get_key)
    maxValue = max(array, key=get_key)

    if int((get_key(maxValue) - get_key(minValue)) / 3) > 0:
        bucketSize = int((get_key(maxValue) - get_key(minValue)) / 3)


    # Initialize buckets
    bucketCount = math.floor((get_key(maxValue) - get_key(minValue)) / bucketSize) + 1
    buckets = []
    for i in range(0, bucketCount):
        buckets.append([])

    # Distribute input array values into buckets
    for i in range(0, len(array)):
        buckets[math.floor((get_key(array[i]) - get_key(minValue)) / bucketSize)].append(array[i])

    # Sort buckets and place back into input array
    array = []
    for i in range(0, len(buckets)):
        buckets[i].sort(key=get_key)
        for j in range(0, len(buckets[i])):
            array.append(buckets[i][j])

    return array




def radixsort(a, get_keys=(lambda item: item[0], lambda item: item[1])):
    for get_key in get_keys:
        maxLen = -1
        for number in a:  # Find longest number, in digits
            numLen = len(str(number))
            if numLen > maxLen:
                maxLen = numLen
        buckets = [[] for i in range(0, 10)]  # Buckets for each digit
        for digit in range(0, maxLen):
            for number in a:
                buckets[int(get_key(number) / 10 ** digit % 10)].append(number)
            del a[:]
            for bucket in buckets:
                a.extend(bucket)
                del bucket[:]
    return a


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

