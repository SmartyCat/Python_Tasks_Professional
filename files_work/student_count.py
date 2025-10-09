import csv

with open("/home/kostya/Загрузки/student_counts.csv", encoding="utf-8") as file, open(
    "sorted_student_counts.csv", "w", encoding="utf-8", newline=""
) as output_file:
    rows = list(csv.DictReader(file))
    years = {row["year"]: [] for row in rows}
    headers = []
    for row in rows:
        for j in row:
            if j != "year":
                years[row["year"]].append((j, row[j]))
    for year in years:
        years[year].sort(key=lambda x: x[0].split("-")[1])
        years[year].sort(key=lambda x: int(x[0].split("-")[0]))

    data = [{**{"year": year}, **dict(years[year])} for year in years]
    for year in years:
        for y in years[year]:
            headers.append(y[0])
        break
    headers.insert(0, "year")
    writer = csv.DictWriter(output_file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)
