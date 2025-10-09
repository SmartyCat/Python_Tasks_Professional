import csv

with open("/home/kostya/Загрузки/prices.csv", encoding="utf-8") as file:
    rows = list(csv.DictReader(file, delimiter=";"))
    data = {row["Магазин"]: [] for row in rows}
    for row in rows:
        for r in row:
            if r != "Магазин":
                data[row["Магазин"]].append((r, row[r]))
    product, price = None, None
    for d in data:
        x = min(data[d], key=lambda x: int(x[1]))
        if product is None or int(x[1]) <= int(price) and product > x[0]:
            shop, product, price = d, *x
    print(f"{product}: {shop}")
