def pairwise(iterable):
    iterable = iter(iterable)
    x = next(iterable)
    for i in iterable:
        yield (x, i)
        x = i
    else:
        yield (x, None)


numbers = [1, 2, 3, 4, 5]
print(*pairwise(numbers))

iterator = iter("stepik")
print(*pairwise(iterator))
