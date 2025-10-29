from itertools import pairwise


def max_pair(iterable):  # first solution, basic variant
    iterable = iter(iterable)
    result, prev = None, next(iterable)
    for i in iterable:
        if result is None or i + prev > result:
            result = i + prev
        prev = i
    else:
        return result


def max_pair(iterable):  # more functional solution
    return sum(max(pairwise(iterable), key=sum))


print(max_pair([1, 8, 2, 4, 3]))

iterator = iter([1, 2, 3, 4, 5])
print(max_pair(iterator))

iterator = iter([0, 0, 0, 0, 0, 0, 0, 0, 0])
print(max_pair(iterator))
