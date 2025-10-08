import csv

number = int(input())

with open("/home/kostya/Загрузки/deniro.csv", encoding="utf-8") as file:
    rows = csv.reader(file)
    try:
        rows = sorted(
            rows,
            key=lambda x: (
                int(x[number - 1]) if x[number - 1].isdigit() else x[number - 1]
            ),
        )
        for row in rows:
            print(",".join(row))
    except IndexError:
        print("Ошибка ввода")
