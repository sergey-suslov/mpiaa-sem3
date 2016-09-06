from mpiaa.timer import time_me
from mpiaa.util import *


def find(items, item_to_find):
    """Returns True if given list of items contains given item.
    Returns False otherwise."""
    return False


def find_if(items, pred):
    """Returns first item for which given predicate is satisfied.
    Returns None if there is no such item."""
    return None


def find_all_if(items, pred):
    """Returns all items for which given predicate is satisfied.
    Returns empty list if there are no such items."""
    return []


def count_if(items, pred):
    """Returns number of items for which given predicate is satisfied."""
    return 0


def all_unique(items):
    """Returns True if all items are unique.
    Returns False otherwise."""
    return False


if __name__ == "__main__":
    time_me("Find", lambda items: find(items, items[-1]), ns=powers_of(10, 0, 6), generator=seq_ints, repeats=1000)
