from collections import Counter


def hash_as_key(objects):
    result = {}
    x = Counter(map(hash, objects))
    for i in objects:
        if x[hash(i)] == 1:
            result[hash(i)] = i
        else:
            result.setdefault(hash(i), []).append(i)
    return result


data = [1, 2, 3, 4, 5, 5]
print(hash_as_key(data))
data = [-1, -2, -3, -4, -5]
print(hash_as_key(data))
data = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]
print(hash_as_key(data))
