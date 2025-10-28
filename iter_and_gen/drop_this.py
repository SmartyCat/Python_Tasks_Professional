from itertools import dropwhile


def drop_this(iterable, obj):  # first solution
    return dropwhile(lambda x: x == obj, iterable)


def drop_this(iterable, obj):  # second solution
    iterable = iter(iterable)
    for i in iterable:
        if i != obj:
            yield i
            break
    yield from iterable


numbers = [0, 0, 0, 1, 2, 3]
print(*drop_this(numbers, 0))

iterator = iter("bbbbeebee")
print(*drop_this(iterator, "b"))

iterator = iter("ssssssssssssssssssssssss")
print(list(drop_this(iterator, "s")))
