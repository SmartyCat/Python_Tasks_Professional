from itertools import islice


def take_nth(iterable, n):  # first solution
    iterable = iter(iterable)
    while n != 1:
        try:
            next(iterable)
            n -= 1
        except StopIteration:
            return None
    else:
        return next(iterable)


def take_nth(iterable, n):  # second solution
    for i in islice(iterable, n - 1, n):
        return i


numbers = [11, 22, 33, 44, 55]
print(take_nth(numbers, 3))

iterator = iter("beegeek")
print(take_nth(iterator, 4))

iterator = iter("beegeek")
print(take_nth(iterator, 10))
