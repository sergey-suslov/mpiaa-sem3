import random


def powers_of(num, min_power, max_power):
    """Returns list of powers of number 'num', from 'min_power' to 'max_power'"""
    return [num**p for p in range(min_power, max_power + 1)]


def seq_ints(n, start=0, step=1):
    """Returns list of 'n' integers, starting with 'start' with a step 'step'"""
    return list(range(start, start + n*abs(step), step))


def random_ints(n, min_int=0, max_int=int(1e6)):
    """Returns list of 'n' random integers, each in a range [min_int, max_int]"""
    return [random.randint(min_int, max_int) for i in range(n)]
