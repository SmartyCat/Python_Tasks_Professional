import csv
import json

final_sum = 0
results = {}
files = ["quarter1.csv", "quarter2.csv", "quarter3.csv", "quarter4.csv"]
for file_name in files:
    with open(
        f"/home/kostya/Загрузки/{file_name}", encoding="utf-8", newline=""
    ) as file:
        rows = list(csv.reader(file))
        for row in rows[1:]:
            results[row[0]] = results.get(row[0], 0) + sum(
                (int(row[1]), int(row[2]), int(row[3]))
            )

with open("/home/kostya/Загрузки/prices.json", encoding="utf-8") as file:
    prices = json.load(file)
    for result in results:
        final_sum += results[result] * prices[result]
print(final_sum)
