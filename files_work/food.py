import json

with open("/home/kostya/Загрузки/food_services.json", encoding="utf-8") as file:
    data = json.load(file)
    area = {}
    shops = {}
    for d in data:
        area[d["District"]] = area.get(d["District"], 0) + 1
        if d["OperatingCompany"]:
            shops.setdefault(d["OperatingCompany"], []).append(d["Name"])

    shops = list(map(lambda x: (x[0], len(x[1])), shops.items()))
    max_shops, max_area = max(shops, key=lambda x: x[1]), max(
        area.items(), key=lambda x: x[1]
    )
    print(f"{max_area[0]}: {max_area[1]}", f"{max_shops[0]}: {max_shops[1]}", sep="\n")
