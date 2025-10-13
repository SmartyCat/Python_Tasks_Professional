from datetime import datetime
import csv


with open("/home/kostya/Загрузки/meetings.csv", encoding="utf-8", newline="") as file:
    rows = csv.DictReader(file)
    rows = sorted(
        rows,
        key=lambda x: datetime.strptime(
            x["meeting_date"] + " " + x["meeting_time"], "%d.%m.%Y %H:%M"
        ),
    )
    for row in rows:
        print(row["surname"], row["name"])
