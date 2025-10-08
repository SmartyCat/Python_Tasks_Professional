from datetime import datetime
import csv


with open(
    "/home/kostya/Загрузки/name_log.csv", "r", encoding="utf-8"
) as input_file, open("new_name_log.csv", "w", encoding="utf-8") as otput_file:
    rows = list(
        csv.DictReader(input_file),
    )
    writer = csv.writer(otput_file)
    shablon = "%d/%m/%Y %H:%M"
    result = []
    headers = ["username", "email", "dtime"]
    dtime = {row["email"]: [] for row in rows}
    for row in rows:
        dtime[row["email"]].append(datetime.strptime(row["dtime"], shablon))
    dtime = {i: max(dtime[i]) for i in dtime}
    for row in rows:
        if datetime.strptime(row["dtime"], shablon) == dtime[row["email"]]:
            result.append((row["username"], row["email"], row["dtime"]))
    result = sorted(result, key=lambda x: x[1])
    writer.writerow(headers)
    writer.writerows(result)
