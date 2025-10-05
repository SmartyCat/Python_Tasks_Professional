from datetime import date, timedelta
import calendar


def func(y):
    results = []
    for i in range(1, 13):
        start = date(y, i, 1)
        x = (3 - start.weekday()) % 7
        start += timedelta(days=x + 14)
        results.append(start.strftime("%d.%m.%Y"))

    return results


print(*func(2021), sep="\n")
