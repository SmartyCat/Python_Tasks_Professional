import csv
from functools import reduce

with open("/home/kostya/Загрузки/salary_data.csv", "r", encoding="utf-8") as file:
    rows = list(csv.DictReader(file, delimiter=";"))
    company_count = {}

    for row in rows:
        if row["company_name"] not in company_count:
            company_count[row["company_name"]] = [1, int(row["salary"])]
        else:
            company_count[row["company_name"]][0] += 1
            company_count[row["company_name"]][1] += int(row["salary"])
    company_count = sorted(
        sorted(company_count.items(), key=lambda x: x[0]),
        key=lambda x: x[1][1] / x[1][0],
    )
    for c in company_count:
        print(c[0])
