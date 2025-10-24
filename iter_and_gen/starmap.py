def starmap(func, iterable):
    """В одну строку пытаюсь"""
    return iter(func(*i) for i in iterable)


pairs = [(1, 3), (2, 5), (6, 4)]
print(*starmap(lambda a, b: a + b, pairs))
points = [(1, 1, 1), (1, 1, 2), (2, 2, 3)]
print(*starmap(lambda x, y, z: x * y * z, points))
