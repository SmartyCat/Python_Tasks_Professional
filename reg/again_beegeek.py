from re import search, I
import sys

# the first solution

print(
    sum(1 for i in sys.stdin.readlines() if search(r".*beegeek.*", i.rstrip(), flags=I))
)


# the second solution

result = 0

for i in sys.stdin.readlines():
    if search(r".*beegeek.*", i.rstrip(), flags=I):
        result += 1
else:
    print(result)
