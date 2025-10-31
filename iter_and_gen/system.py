from itertools import product
from string import hexdigits

l = [[hexdigits[i].upper() for i in range(int(input()))]] * int(input())

print(*("".join(i) for i in product(*l)))
