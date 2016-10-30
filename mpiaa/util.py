import random


def powers_of(num, min_power, max_power):
    """Returns list of powers of number 'num', from 'min_power' to 'max_power'"""
    return [num**p for p in range(min_power, max_power + 1)]


def seq_ints(n, start=0, step=1):
    """Returns list of 'n' integers, starting with 'start' with a step 'step'"""
    return list(range(start, start + n*abs(step), step))


def shuffled_ints(n, start=0, step=1):
    ints = seq_ints(n, start, step)
    random.shuffle(ints)
    return ints


def random_ints(n, min_int=0, max_int=int(1e6)):
    """Returns list of 'n' random integers, each in a range [min_int, max_int]"""
    return [random.randint(min_int, max_int) for i in range(n)]


def random_int_pairs(n, min_int=0, max_int=int(1e6)):
    """Returns list of 'n' random integers, each in a range [min_int, max_int]"""
    first_items = random_ints(n, min_int, max_int)
    second_items = random_ints(n, min_int, max_int)
    return list(zip(first_items, second_items))


def random_string(size):
    """Returns string of random characters of length size"""
    return "".join([chr(i % 256) for i in range(size)])


def random_strings(n, max_string_size=6):
    """Returns list of random strings, each of random length from 1 up to max_string_size"""
    return [random_string(random.randint(1, max_string_size)) for i in range(n)]


