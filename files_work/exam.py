import json
import csv
from datetime import datetime


with open("/home/kostya/Загрузки/exam_results.csv", encoding="utf-8") as input_file:
    rows = list(csv.DictReader(input_file))
    result = {}
    for row in rows:
        name = row["name"] + " " + row["surname"]
        x = {
            "name": row["name"],
            "surname": row["surname"],
            "best_score": row["score"],
            "date_and_time": row["date_and_time"],
            "email": row["email"],
        }
        if name not in result:

            result[name] = x

        else:
            if (
                int(row["score"]) > int(result[name]["best_score"])
                or int(row["score"]) == int(result[name]["best_score"])
                and datetime.fromisoformat(row["date_and_time"])
                > datetime.fromisoformat(result[name]["date_and_time"])
            ):
                result[name] = x

    data = sorted([result[r] for r in result], key=lambda x: x["email"])

with open("best_scores.json", "w", encoding="utf-8") as output_file:
    json.dump(data, output_file, indent=3)
