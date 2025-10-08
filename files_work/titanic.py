import csv

with open("/home/kostya/Загрузки/titanic.csv", "r", encoding="utf-8") as file:
    rows = list(
        filter(
            lambda x: x["survived"] == "1" and float(x["age"]) < 18,
            csv.DictReader(file, delimiter=";"),
        )
    )
    result = [row["name"] for row in rows if row["sex"] == "male"] + [
        row["name"] for row in rows if row["sex"] == "female"
    ]
    print(*result, sep="\n")
