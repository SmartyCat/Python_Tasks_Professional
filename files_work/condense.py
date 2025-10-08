import csv


def condense_csv(filename, id_name):
    with open(filename, encoding="utf-8") as input_file, open(
        "condensed.csv", "w", encoding="utf-8"
    ) as output_file:
        rows = list(csv.reader(input_file))
        wri = csv.writer(output_file)
        headers = [id_name]
        r = {row[0]: [r[2] for r in rows if r[0] == row[0]] for row in rows}
        result = []
        for row in rows:
            if row[1] not in headers:
                headers.append(row[1])
        for i in r.items():
            result.append((i[0], *i[1]))
        wri.writerow(headers)
        wri.writerows(result)


condense_csv("test_1", "ID")
