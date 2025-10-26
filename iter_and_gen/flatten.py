def flatten(nested_list: list):
    for i in nested_list:
        if isinstance(i, int):
            yield i
        else:
            yield from flatten(i)


generator = flatten([1, 2, 3, 4, 5, 6, 7])
print(*generator)
