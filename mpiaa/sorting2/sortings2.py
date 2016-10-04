from mpiaa.util import seq_ints, random_ints, random_int_pairs, powers_of
from mpiaa.timer import time_us


def counting_sort(items, get_key=lambda item: item):
    """
    Counting sort

    :param items: list of items to sort
    :param get_key: function f(item) which returns item's key
    :return: sorted list of items
    """
    result = items
    # Your code here
    return result


def bucket_sort(items, get_key=lambda item: item):
    """
    Bucket sort

    :param items: list of items to sort
    :param get_key: function f(item) which returns item's key
    :return: sorted list of items
    """
    result = items
    # Your code here
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
        "Cnt. sort": counting_sort,
        "Bucket sort": bucket_sort
    }, ns=powers_of(10, 0, 5), generator=lambda n: random_ints(n, -1000, 1000), repeats=100)

    time_us({
        "Std sort": sorted,
        "Radix sort": radix_sort
    }, ns=powers_of(10, 0, 5), generator=lambda n: random_int_pairs(n, -1000, 1000), repeats=100)

