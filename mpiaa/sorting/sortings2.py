from mpiaa.util import seq_ints, random_ints, powers_of
from mpiaa.timer import time_us


def count_sort(items):
    result = items
    return result


def bucket_sort(items):
    result = items
    return result


def radix_sort(items):
    result = items
    return result


if __name__ == "__main__":
    time_us({
        "Std sort": sorted
    }, ns=powers_of(10, 0, 4), generator=random_ints, repeats=10)
