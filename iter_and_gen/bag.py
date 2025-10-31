from collections import namedtuple
from itertools import combinations

Item = namedtuple("Item", ["name", "mass", "price"])
m = int(input())
items = [
    Item("Обручальное кольцо", 7, 49_000),
    Item("Мобильный телефон", 200, 110_000),
    Item("Ноутбук", 2000, 150_000),
    Item("Ручка Паркер", 20, 37_000),
    Item("Статуэтка Оскар", 4000, 28_000),
    Item("Наушники", 150, 11_000),
    Item("Гитара", 1500, 32_000),
    Item("Золотая монета", 8, 140_000),
    Item("Фотоаппарат", 720, 79_000),
    Item("Лимитированные кроссовки", 300, 80_000),
]

price = 0
data = None
n = 1
while n != 11:
    for i in combinations(items, r=n):
        mass, pr = sum(j.mass for j in i), sum(j.price for j in i)
        if mass <= m and pr > price:
            data, price = (i.name for i in sorted(i, key=lambda x: x.name)), pr
    n += 1
else:
    if data:
        print(*data, sep="\n")
    else:
        print("Рюкзак собрать не удастся")
