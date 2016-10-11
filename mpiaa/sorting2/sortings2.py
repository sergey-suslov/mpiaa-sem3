from mpiaa.util import seq_ints, random_ints, random_int_pairs, powers_of
from mpiaa.timer import time_us


def counting_sort(items, get_key=lambda item: item):
    """
    Counting sort

    :param items: list of items to sort
    :param get_key: function f(item) which returns item's key
    :return: sorted list of items
    """

    # Replace value by correct one
    num_of_keys = 123

    # Replace function body by correct one
    def key_to_index(key):
        return key

    count = [0]*num_of_keys
    for item in items:
        count[key_to_index(get_key(item))] += 1

    # Modify count here appropriately

    result = [0]*len(items)
    # Rest of your code here
    return result


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

    # Modify buckets appropriately if needed

    result = []
    # Rest of your code here
    return result


def radix_sort(items, get_keys=(lambda item: item[0], lambda item: item[1])):
    """
    Radix sort

    :param items: list of items to sort
    :param get_keys: list of functions f(item), each of which returns item's key
    :return: sorted list of items
    """
    result = items
    # Your code here
    return result


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

