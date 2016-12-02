from mpiaa.util import seq_ints, random_ints, powers_of
from mpiaa.timer import time_us


def bubble_sort(items, cmp=lambda x, y: x < y):
    """
    Bubble sort

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


def smallest(lst):
    """Finds the smallest element in the list."""
    small = lst[0]
    for i in range(len(lst)):
        if lst[i] < small:
            small = lst[i]
        else:
            small = small
    return small


def selection_sort(lst):
    """Sorts the list through selection sort.  Selection sort is
    done by finding the smallest element in the unsorted list, removing
    it from the unsorted list, placing it into the sorted list, and then
    repeating this with the rest of the unsorted list."""

    sorted_lst = []

    def smallest_insert(lst):
        sorted_lst.append(smallest(lst))
        lst.remove(smallest(lst))

    for i in range(len(lst)):
        smallest_insert(lst)
    return sorted_lst


def split(lst):
    """This splits a list into sublists of pairs of elements."""
    split_list = []
    x = 0
    if len(lst) % 2 == 0:
        while x < len(lst):
            split_list.append([lst[x], lst[x + 1]])
            x = x + 2
        return split_list
    else:
        while x < len(lst) - 1:
            split_list.append([lst[x], lst[x + 1]])
            x = x + 2
        return split_list + [lst[len(lst) - 1]]


def merge(lst1, lst2):
    """This merges two lists into one."""
    lst = lst1 + lst2
    return selection_sort(lst)


def foldr(combiner, base, lst):
    if lst == []:
        return base
    else:
        return combiner(lst[0], foldr(combiner, base, lst[1:]))

def all_unique(items):
    sorted_list = selection_sort(items)
    for i, v in enumerate(sorted_list[1:]):
        if v == sorted_list[i]:
            return False
    return True

def merge_sort(lst):
    """This does the simple merge sort. The list is split into sublists,
    each sublist is selection-sorted recursively, and the sorted sublists are
    then re-merged."""
    if len(lst) == 1:
        return lst
    elif len(lst) % 2 == 0:
        return foldr(merge, [], split(lst))
    else:
        popped = lst[0]
        lst.pop(0)
        return selection_sort([popped] + foldr(merge, [], split(lst)))


def quick_sort(lst):
    """Quick sort chooses a pivot element, places the elements greater than
    and less than the pivot into places relative to the pivot, and are then
    recursively sorted."""
    lst1 = [x for x in lst[1:] if x <= lst[0]]
    lst2 = [y for y in lst if y > lst[0]]
    if len(lst) == 0:
        return lst
    elif len(lst) == 1:
        return lst
    else:
        return quick_sort(lst1) + [lst[0]] + quick_sort(lst2)


if __name__ == "__main__":
    time_us({
        "Bubble sort": bubble_sort,
        "Std sort": sorted
    }, ns=powers_of(10, 0, 4), generator=random_ints, repeats=10)
