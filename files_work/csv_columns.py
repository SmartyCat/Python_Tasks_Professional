import csv


def csv_columns(filename):
    with open(filename, "r", encoding="utf-8") as file:
        rows = csv.DictReader(file)
        result = {i: [] for i in rows.fieldnames}
        for row in rows:
            for i in row.items():
                result[i[0]].append(i[1])
        return result


print(csv_columns("test_2"))
