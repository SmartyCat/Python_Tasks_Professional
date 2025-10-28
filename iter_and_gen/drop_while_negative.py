from itertools import dropwhile


def drop_while_negative(iterable):  # first solution
    return dropwhile(lambda x: x < 0, iterable)


def drop_while_negative(iterable):  #  second solution
    iterable = iter(iterable)
    for i in iterable:
        if i < 0:
            continue
        else:
            yield i
            break
    yield from iterable


numbers = [-3, -2, -1, 0, 1, 2, 3]
print(*drop_while_negative(numbers))

iterator = iter([-3, -2, -1, 0, 1, 2, 3, -4, -5, -6])
print(*drop_while_negative(iterator))

iterator = iter([-3, -2, -1, -4, -5, -6])
print(list(drop_while_negative(iterator)))
