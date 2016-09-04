import timeit


def make_header(strings):
    return " ".join(["{0:<12}".format(s) for s in strings])


def make_line(n, times):
    return " ".join(["{0:<12}".format(n)] + ["{0:<12.5f}".format(t) for t in times])


def time_me(functions, ns, repeats=10000):
    print(make_header(["N"] + list(functions.keys())))
    for n in ns:
        data = range(n + 1)
        times = []
        for func in functions.values():
            timer = timeit.Timer(lambda: func(data))
            times.append(timer.timeit(repeats))
        print(make_line(n, times))
