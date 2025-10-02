from datetime import date, timedelta


def get_date_range(start, end):
    result = []
    if start > end:
        return []
    while start <= end:
        result.append(start)
        start += timedelta(days=1)

    return result


date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)
print(*get_date_range(date1, date2), sep="\n")

date1 = date(2019, 6, 5)
date2 = date(2019, 6, 5)
print(get_date_range(date1, date2))