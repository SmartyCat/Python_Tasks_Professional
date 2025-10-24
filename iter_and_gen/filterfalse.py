def filterfalse(predicate, iterable):
    """Решил сделать одной строкой"""
    return (
        iter(i for i in iterable if not i)
        if predicate is None
        else iter(i for i in iterable if not predicate(i))
    )


objects = [0, 1, True, False, 17, []]
print(*filterfalse(None, objects))

numbers = (1, 2, 3, 4, 5)
print(*filterfalse(lambda x: x % 2 == 0, numbers))

numbers = [1, 2, 3, 4, 5]
print(*filterfalse(lambda x: x >= 3, numbers))
