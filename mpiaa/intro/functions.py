from mpiaa.timer import time_me, powers_of


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


def all_unique(items):
    """Returns True if all items are unique.
    Returns False otherwise."""


if __name__ == "__main__":
    time_me("Find", lambda items: find(items, len(items)/2), powers_of(10, 6), 1000)
