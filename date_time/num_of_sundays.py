from datetime import date, timedelta


def num_of_sundays(y):
    d = date(year=y, month=1, day=1)
    counter = 0
    while d.year == y:
        if d.weekday() == 6:
            counter += 1
        d += timedelta(days=1)
    return counter


print(num_of_sundays(2001))
