import json

with open("/home/kostya/Загрузки/data1.json", encoding="utf-8") as file1, open(
    "/home/kostya/Загрузки/data2.json", encoding="utf-8"
) as file2:
    d1, d2 = json.load(file1), json.load(file2)
    result = {**d1, **d2}
with open("data_merge.json", "w", encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False, indent=3)
