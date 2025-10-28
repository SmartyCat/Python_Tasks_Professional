from itertools import islice


def take(iterable, n):  # first solution
    yield from islice(iterable, n)


def take(iterable, n):  # second solution

    iterable = iter(iterable)
    while n > 0:
        try:
            yield next(iterable)
            n -= 1
        except StopIteration:
            break


print(*take(range(10), 5))

iterator = iter("beegeek")
print(*take(iterator, 22))

iterator = iter("beegeek")
print(*take(iterator, 1))
