from string import ascii_uppercase
from itertools import cycle, count


def alnum_sequence():
    return cycle(
        (j for i in zip(range(1, 27), ascii_uppercase) for j in i)
    )  # в одну строку


alnum = alnum_sequence()
print(*(next(alnum) for _ in range(55)))

alnum = alnum_sequence()
print(*(next(alnum) for _ in range(100)))
