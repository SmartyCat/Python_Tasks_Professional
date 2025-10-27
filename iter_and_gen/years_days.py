from calendar import isleap
from datetime import timedelta, date


def years_days(year: int):
    start = date(year, 1, 1)
    return (start + timedelta(days=i) for i in range(365 if not isleap(year) else 366))


dates = years_days(2024)
print(*dates)