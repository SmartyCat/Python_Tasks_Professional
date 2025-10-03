from datetime import datetime

dates = list(map(lambda x: datetime.strptime(x, "%d.%m.%Y").date(), input().split()))

print(
    [
        abs(item - dates[index + 1]).days
        for index, item in enumerate(dates[: len(dates) - 1])
    ]
)
