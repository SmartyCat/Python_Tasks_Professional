import json
import csv


with open("/home/kostya/Загрузки/students.json", encoding="utf-8") as input_file:
    data = json.load(input_file)
    data.sort(key=lambda x: x["name"])
    result = [
        (d["name"], d["phone"])
        for d in data
        if d["age"] >= 18 and d["progress"] >= 75
    ]
with open("data.csv", "w", encoding="utf-8", newline="") as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["name", "phone"])
    writer.writerows(result)
