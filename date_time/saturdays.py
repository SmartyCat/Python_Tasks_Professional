from datetime import date, timedelta


def saturdays_between_two_dates(start, end):
    start, end = min(start, end), max(start, end)
    return sum(
        [
            1
            for i in range((end - start).days + 1)
            if (start + timedelta(days=i)).weekday() == 5
        ]
    )


date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)
print(saturdays_between_two_dates(date1, date2))


date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)
print(saturdays_between_two_dates(date1, date2))

date1 = date(2018, 7, 13)
date2 = date(2018, 7, 13)
print(saturdays_between_two_dates(date1, date2))
