import timeit

def time_fn(fn):
    duration = timeit.timeit(fn, number=1)
    print(f"Duration {duration} seconds")
