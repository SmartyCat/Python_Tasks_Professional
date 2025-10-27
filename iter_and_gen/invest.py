import csv

with open(
    "/home/kostya/Загрузки/data (1).csv", "r", encoding="utf-8", newline=""
) as file:
    data = csv.DictReader(file)
    print(sum(int(d["raisedAmt"]) for d in data if d["round"] == "a"))
