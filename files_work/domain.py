import csv

with open("/home/kostya/Загрузки/data.csv", "r", encoding="utf-8") as input_file, open(
    "domain_usage.csv", "w", encoding="utf-8"
) as output_file:
    rows = csv.DictReader(input_file)
    writer = csv.writer(output_file, delimiter=",")
    result = {}
    columns = ["domain", "count"]
    for row in rows:
        domain = row["email"][row["email"].index("@") + 1 :]
        result[domain] = result.get(domain, 0) + 1
    result = sorted(sorted(result.items(), key=lambda x: x[0]), key=lambda x: x[1])
    writer.writerow(columns)
    writer.writerows(result)

with open("domain_usage.csv", "r", encoding="utf-8") as file:
    rows = csv.DictReader(file)
    for row in rows:
        print(row)
