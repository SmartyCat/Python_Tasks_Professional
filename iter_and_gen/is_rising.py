from itertools import tee


def is_rising(iterable):  # first solution, more basic var
    iterable = iter(iterable)
    x = next(iterable)
    for i in iterable:
        if i <= x:
            return False
        x = i
    else:
        return True


def is_rising(iterable):  # with func
    iterable = tee(iterable)
    return list(iterable[0]) == sorted(set(iterable[1]))


print(is_rising([1, 2, 3, 4, 5]))

iterator = iter([1, 1, 1, 2, 3, 4])
print(is_rising(iterator))

iterator = iter(list(range(100, 200)))
print(is_rising(iterator))
