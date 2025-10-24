from functools import lru_cache
import sys


@lru_cache
def just_dima(s: str) -> str:
    return "".join(sorted(s.rstrip()))


# можно так но память больше есть будет хоть и комактно
print(*[just_dima(i) for i in sys.stdin.readlines()], sep="\n")
# а можно так , хоть и примитивно но надежно и памяти меньше жрет
for i in sys.stdin.readlines():
    print(just_dima(i))
