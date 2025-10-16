from collections import ChainMap, Counter
from functools import reduce

bread = {"булочка с кунжутом": 15, "обычная булочка": 10, "ржаная булочка": 15}
meat = {"куриный бифштекс": 50, "говяжий бифштекс": 70, "рыбный бифштекс": 40}
sauce = {
    "сливочно-чесночный": 15,
    "кетчуп": 10,
    "горчица": 10,
    "барбекю": 15,
    "чили": 15,
}
vegetables = {"лук": 10, "салат": 15, "помидор": 15, "огурцы": 10}
toppings = {"сыр": 25, "яйцо": 15, "бекон": 30}
ingrid = Counter(input().split(","))
max_char = len(max(ingrid, key=len))
d = ChainMap(bread, meat, sauce, vegetables, toppings)
price = sum(d[i] * ingrid[i] for i in ingrid)
for name, count in sorted(ingrid.items()):
    print(name + " " * (max_char - len(name) + 1) + f"x {count}")
print("-" * (max_char + 5), f"ИТОГ: {price}р", sep="\n")
