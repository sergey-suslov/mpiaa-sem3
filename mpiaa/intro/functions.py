from mpiaa.timer import time_me


def find(items, item_to_find):
    """Returns True if given item is in given list of items.
    Returns False otherwise"""
    return False


if __name__ == "__main__":
    time_me({
        "Find": lambda items: find(items, 0)
    }, [10**n for n in range(1, 6)])
