

def grouper(iterable, n):
    iterable = iter(iterable)
    while iterable:
        result = []
        try:
            for i in range(n):
                result.append(next(iterable))
            else:
                yield tuple(result)
        except StopIteration:
            break
    if result:
        while len(result) != n:
            result.append(None)
        yield tuple(result)


numbers = [1, 2, 3, 4, 5, 6]
print(*grouper(numbers, 2))

iterator = iter([1, 2, 3, 4, 5, 6, 7])
print(*grouper(iterator, 3))

iterator = iter([1, 2, 3])
print(*grouper(iterator, 5))
