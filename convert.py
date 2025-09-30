from functools import reduce


def convert(string):
    uppers = reduce(lambda x, y: 1 + x if y.isupper() else x + 0, string, 0)
    lowers = reduce(lambda x, y: 1 + x if y.islower() else x + 0, string, 0)
    return string.upper() if uppers > lowers else string.lower()


print(convert("BEEgeek"))
print(convert("pyTHON"))
print(convert("pi31415!"))
