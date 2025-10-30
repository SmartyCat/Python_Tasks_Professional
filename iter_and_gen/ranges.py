from itertools import groupby


def ranges(numbers):
    result = []
    cur = []
    for i in numbers:
        if not cur or abs(cur[-1] - i) == 1:
            cur.append(i)
        else:
            if len(cur) > 1:
                result.append((cur[0], cur[-1]))
            else:
                cur.append(cur[-1])
                result.append(tuple(cur))
            cur = [i]
    else:
        if len(cur) > 1:
            result.append((cur[0], cur[-1]))
        else:
            cur.append(cur[-1])
            result.append(tuple(cur))
    return result


numbers = [1, 2, 3, 4, 7, 8, 10]
print(*ranges(numbers))

numbers = [1, 3, 5, 7]
print(*ranges(numbers))
numbers = [1, 2, 3, 4, 5, 6, 7]

print(*ranges(numbers))

numbers = list(range(5, 101))

print(*ranges(numbers))

numbers = list(range(10, 21)) + [30] + list(range(35, 101)) + list(range(1000, 1001))

print(*ranges(numbers))
