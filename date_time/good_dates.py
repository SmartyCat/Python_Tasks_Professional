from datetime import date


def print_good_dates(dates):
    for i in sorted(dates):
        if i.year == 1992 and i.month + i.day == 29:
            print(i.strftime("%B %d, %Y"))


dates = []
print_good_dates(dates)
dates = [date(1993, 9, 15), date(2021, 11, 2), date(2000, 7, 7)]
print_good_dates(dates)
