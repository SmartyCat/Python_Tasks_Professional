from itertools import chain


def sum_of_digits(iterable):  # first solution with libary
    return sum(int(i) for i in chain.from_iterable(map(str, iterable)))


def sum_of_digits(iterable):  # second solution? basic variant
    result = 0
    for i in iterable:
        result += sum(int(j) for j in str(i))
    return result


print(sum_of_digits([13, 20, 41, 2, 2, 5]))

print(sum_of_digits((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

print(sum_of_digits([123456789]))
