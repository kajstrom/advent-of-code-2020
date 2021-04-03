import timeit


def time_fn(fn):
    duration = timeit.timeit(fn, number=1)
    print(f"Duration {duration} seconds")


def count(needle, haystack):
    return sum(map(lambda item: item == needle, haystack))
