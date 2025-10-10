import json
from datetime import time

with open("/home/kostya/Загрузки/pools.json", encoding="utf-8") as input_file:
    rows = json.load(input_file)
    rows = list(
        filter(
            lambda x: "Понедельник" in x["WorkingHoursSummer"]
            and time.fromisoformat(x["WorkingHoursSummer"]["Понедельник"].split("-")[0])
            <= time(hour=10)
            and time.fromisoformat(x["WorkingHoursSummer"]["Понедельник"].split("-")[1])
            >= time(hour=12),
            rows,
        )
    )
    length, width, street = None, None, None
    for row in rows:
        l, w = row["DimensionsSummer"]["Length"], row["DimensionsSummer"]["Width"]
        if length is None or l > length or l == length and w > width:
            length, width, street = (
                l,
                w,
                row["Address"],
            )

    print(f"{length}x{width}", street, sep="\n")
