import timeit


def make_header(func_names):
    return " ".join(["{0:<12}".format(s) for s in ["N"] + func_names])


def make_line(n, times):
    return " ".join(["{0:<12}".format(n)] + ["{0:<12.5f}".format(t) for t in times])


def time_us(functions, ns, generator, repeats=int(1e6)):
    print(make_header(list(functions.keys())))
    for n in ns:
        data = generator(n)
        times = []
        for func in functions.values():
            timer = timeit.Timer(lambda: func(data))
            times.append(timer.timeit(repeats))
        print(make_line(n, times))


def time_me(func_name, function, ns, generator, repeats=int(1e6)):
    time_us(functions={func_name: function}, ns=ns, generator=generator, repeats=repeats)



