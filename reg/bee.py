from re import search
import sys

# the first solution

data = sys.stdin.readlines()

print(
    sum(1 for d in data if search(r".*(bee).*\1.*", d.rstrip())),
    sum(1 for d in data if search(r".*\bgeek\b.*", d.rstrip())),
    sep="\n",
)
# the second solution
bee, geek = 0, 0

for i in sys.stdin.readlines():
    i = i.rstrip()
    bee += 1 if search(r".*(bee).*\1.*", i) else 0
    geek += 1 if search(r".*\bgeek\b.*", i.rstrip()) else 0

print(bee, geek, sep="\n")
