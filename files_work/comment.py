import sys

data = len(
    list(filter(lambda x: x[0] == "#", map(lambda x: x.strip(), sys.stdin.readlines())))
)

print(data)
