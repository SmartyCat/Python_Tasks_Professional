from itertools import groupby
from collections import Counter


def group_anagrams(
    words,
):  # так как порядок не важен по условию, особо не парюсь с сортировкой
    for i in groupby(
        sorted(words, key=lambda x: sorted(Counter(x))),
        key=lambda x: Counter(x),
    ):
        yield tuple(i[1])


groups = group_anagrams(
    ["крона", "сеточка", "тесачок", "лучик", "стоечка", "норка", "чулки"]
)
print(*groups)
