from functools import wraps
from time import perf_counter
import sys


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]

    return wrapper

@memoize
def fibonaaci(n) -> int:
    if n < 2:
        return n
    return fibonaaci(n - 1) + fibonaaci(n - 2)


if __name__ == '__main__':
    sys.setrecursionlimit(10000)

    start = perf_counter()
    f = fibonaaci(300)
    end = perf_counter()

    print(f)
    print(f'Time: {end - start} seconds')
