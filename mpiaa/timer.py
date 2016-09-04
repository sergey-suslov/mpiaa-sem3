import timeit


def make_header(strings):
    return " ".join(["{0:<12}".format(s) for s in strings])


def make_line(n, times):
    return " ".join(["{0:<12}".format(n)] + ["{0:<12.5f}".format(t) for t in times])


def time_us(functions, ns, repeats=10000):
    print(make_header(["N"] + list(functions.keys())))
    for n in ns:
        data = list(range(n + 1))
        times = []
        for func in functions.values():
            timer = timeit.Timer(lambda: func(data))
            times.append(timer.timeit(repeats))
        print(make_line(n, times))


def time_me(func_name, function, ns, repeats=10000):
    time_us({func_name: function}, ns, repeats)


def powers_of(num, max_power):
    return [num**p for p in range(0, max_power + 1)]
