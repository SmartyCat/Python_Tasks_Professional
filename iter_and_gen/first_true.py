def first_true(iterable, predicate):
    if predicate is None:
        predicate = bool
    for i in iterable:
        if predicate(i):
            return i


def first_true(iterable, predicate):
    for i in list(
        filter(lambda x: bool(x) if predicate is None else predicate(x), iterable)
    ):
        return i


numbers = [1, 1, 1, 1, 2, 4, 5, 6]
print(first_true(numbers, lambda num: num % 2 == 0))

numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])
print(first_true(numbers, lambda num: num > 10))

numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200)
print(first_true(numbers, None))
