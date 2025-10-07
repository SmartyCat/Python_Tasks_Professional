import csv

with open("/home/kostya/Загрузки/wifi.csv", "r", encoding="utf-8") as file:
    result = {}
    rows = csv.DictReader(file, delimiter=";")
    for row in rows:
        result[row["district"]] = result.get(row["district"], 0) + int(
            row["number_of_access_points"]
        )
    result = sorted(result.items(), key=lambda x: (x[1], x[0]), reverse=True)
    for i in result:
        print(f"{i[0]}: {i[1]}")
