def around(iterable):
    iterable = iter(iterable)
    back, forward = None, next(iterable)
    for i in iterable:
        yield back, forward, i
        back, forward = forward, i
    else:
        yield back, forward, None


numbers = [1, 2, 3, 4, 5]
print(*around(numbers))

iterator = iter('hey')
print(*around(iterator))