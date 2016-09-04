from mpiaa.timer import time_me, powers_of


def find(items, item_to_find):
    """Returns True if given item is in given list of items.
    Returns False otherwise"""
    return False


if __name__ == "__main__":
    time_me("Find", lambda items: find(items, len(items)/2), powers_of(10, 6), 1000)
