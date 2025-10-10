import csv
import json


with open("/home/kostya/Загрузки/playgrounds.csv", encoding="utf-8") as input_file:
    rows = list(csv.DictReader(input_file, delimiter=";"))
    result = {}
    for row in rows:
        result.setdefault(row["AdmArea"], {}).setdefault(row["District"], []).append(
            row["Address"]
        )
with open("addresses.json", "w", encoding="utf-8") as output_file:
    json.dump(result, output_file, indent=3, ensure_ascii=False)
