from mpiaa.util import seq_ints, random_ints, powers_of
from mpiaa.timer import time_us


def bubble_sort(items, cmp=lambda x, y: x < y):
    """
    Bubble sort_func

    :param items: list of items to sort_func
    :param cmp: compare function, cmp(x,y) returns True if x < y, False otherwise
    :return: sorted items
    """
    result = items
    for i in range(len(result)):
        for j in range(0, len(result) - i - 1):
            if cmp(result[j + 1], result[j]):
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def selection_sort(items, cmp=lambda x, y: x < y):
    """
    Selection sort_func

    :param items: list of items to sort_func
    :param cmp: compare function, cmp(x,y) returns True if x < y, False otherwise
    :return: sorted items
    """
    result = items
    # Your code here
    return result


def merge_sort(items, cmp=lambda x, y: x < y):
    """
    Merge sort_func

    :param items: list of items to sort_func
    :param cmp: compare function, cmp(x,y) returns True if x < y, False otherwise
    :return: sorted items
    """
    result = items
    # Your code here
    return result


def quick_sort(items, cmp=lambda x, y: x < y):
    """
    Quick sort_func

    :param items: list of items to sort_func
    :param cmp: compare function, cmp(x,y) returns True if x < y, False otherwise
    :return: sorted items
    """
    result = items
    # Your code here
    return result


if __name__ == "__main__":
    time_us({
        "Bubble sort_func": bubble_sort,
        "Std sort_func": sorted
    }, ns=powers_of(10, 0, 4), generator=random_ints, repeats=10)
