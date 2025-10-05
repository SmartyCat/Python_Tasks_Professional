from datetime import date, timedelta


def get_all_mondays(y):
    start = date(y, 1, 1)
    dif = (date(y, 12, 31) - start).days + 1
    return [
        start + timedelta(days=i)
        for i in range(dif)
        if (start + timedelta(days=i)).weekday() == 0
    ]


print(get_all_mondays(2021))
