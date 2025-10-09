import json

with open("/home/kostya/Загрузки/countries.json", encoding="utf-8") as input_file:
    data = json.load(input_file)
    religions = {
        d["religion"]: [i["country"] for i in data if i["religion"] == d["religion"]]
        for d in data
    }
with open("religion.json", "w", encoding="utf-8") as output_file:
    json.dump(religions, output_file, ensure_ascii=False, indent=3)
