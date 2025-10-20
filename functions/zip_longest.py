def zip_longest(*args, fill=None):
    max_from_args = len(max(args, key=len))
    return list(zip(*[a + [fill] * (max_from_args - len(a)) for a in args]))


print(zip_longest([1, 2, 3, 4, 5], ["a", "b", "c"], fill="_"))
data = [[1, 2, 3, 4, 5], ["one", "two", "three"], ["I", "II"]]
print(zip_longest(*data))
data = [
    [1, 2, 3, 4, 5],
    ["one", "two", "three", "four", "five"],
    ["I", "II", "III", "IV", "V"],
]
print(zip_longest(*data))
