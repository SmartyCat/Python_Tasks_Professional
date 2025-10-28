from itertools import accumulate
from operator import mul


def factorials(n: int):
    # return (factorial(i) for i in range(1, n + 1)) # как по мне более очевидный
    return accumulate(range(1, n + 1), mul)


numbers = factorials(6)
print(*numbers)
