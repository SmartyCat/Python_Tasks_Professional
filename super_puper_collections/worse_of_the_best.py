import sys
from collections import Counter


l = Counter()
for i in sys.stdin.readlines():
    i = i.split()
    l[i[0]] = int(i[1].rstrip())

print(l.most_common()[-2][0])

print(
    sorted(
        map(lambda x: x.split(), sys.stdin.readlines()),
        key=lambda x: int(x[1].rstrip()),
    )[1][0]
)
