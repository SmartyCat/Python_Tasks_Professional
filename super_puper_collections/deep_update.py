from collections import ChainMap


def deep_update(chainmap, key, value):
    flag = False
    for i in chainmap.maps:
        if key in i:
            i[key] = value
            flag = True
    if not flag:
        chainmap[key] = value


chainmap = ChainMap({"city": "Moscow"}, {"name": "Arthur"}, {"name": "Timur"})
deep_update(chainmap, "name", "Dima")
print(chainmap)

chainmap = ChainMap({"name": "Arthur"}, {"name": "Timur"})
deep_update(chainmap, "age", 20)
print(chainmap)
