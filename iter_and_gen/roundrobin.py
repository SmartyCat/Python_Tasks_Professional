from itertools import zip_longest


def roundrobin(*args):
    for i in zip_longest(*args):
        for j in i:
            if j is not None:
                yield j


print(*roundrobin("abc", "d", "ef"))

numbers = [1, 2, 3]
letters = iter("beegeek")
print(*roundrobin(numbers, letters))
