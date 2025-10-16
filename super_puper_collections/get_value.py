from collections import ChainMap
from test import func


def get_value(chainmap, key, from_left=True):
    if from_left:
        for i in chainmap.maps:
            if func(i, key):
                return func(i, key)
    else:
        for i in chainmap.maps[::-1]:
            if func(i, key):
                return func(i, key)


chainmap = ChainMap({"name": "Arthur"}, {"name": "Timur"})
print(get_value(chainmap, "name"))

chainmap = ChainMap({"name": "Arthur"}, {"name": "Timur"})
print(get_value(chainmap, "name", False))
chainmap = ChainMap({"name": "Arthur"}, {"name": "Timur"})
print(get_value(chainmap, "age"))
