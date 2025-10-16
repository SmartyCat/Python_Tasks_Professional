import json
from collections import ChainMap
from functools import reduce

with open("/home/kostya/Загрузки/zoo.json", encoding="utf-8") as file:
    data = json.load(file)
    l = ChainMap(*data)  # ПЕрвый способ
    print(sum(l[d] for d in l))

    print(reduce(lambda x, y: sum(y.values()) + x, data, 0))  # Второй способ
