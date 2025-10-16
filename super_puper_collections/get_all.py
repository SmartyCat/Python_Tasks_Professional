from collections import ChainMap


def get_all_values(chainmap, key):
    return {i[key] for i in chainmap.maps if key in i}


chainmap = ChainMap({"name": "Arthur"}, {"name": "Timur"})
result = get_all_values(chainmap, "age")
print(result)
