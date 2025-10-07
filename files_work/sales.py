import csv


with open("/home/kostya/Загрузки/sales.csv", "r", encoding="utf-8") as file:
    rows = filter(
        lambda x: int(x["new_price"]) < int(x["old_price"]),
        csv.DictReader(file, delimiter=";"),
    )
    for row in rows:
        print(row["name"])
