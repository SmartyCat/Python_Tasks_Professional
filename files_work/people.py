import json

with open("/home/kostya/Загрузки/people.json", encoding="utf-8") as input_file:
    data = json.load(input_file)
    names = [j for i in data for j in i]

    for n in names:
        for d in data:
            if n not in d:
                d[n] = None
with open("updated_people.json", "w", encoding="utf-8") as output_file:
    json.dump(data, output_file, ensure_ascii=False, indent=3)
