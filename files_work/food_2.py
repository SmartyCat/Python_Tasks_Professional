import json

with open("/home/kostya/Загрузки/food_services.json", encoding="utf-8") as file:
    data = json.load(file)
    result = {}
    for d in data:
        if d["TypeObject"] not in result:
            result[d["TypeObject"]] = (d["Name"], d["SeatsCount"])
        elif d["SeatsCount"] > result[d["TypeObject"]][1]:
            result[d["TypeObject"]] = (d["Name"], d["SeatsCount"])
    for i in sorted(result.items(), key=lambda x: x[0]):
        print(f"{i[0]}: {i[1][0]}, {i[1][1]}")
