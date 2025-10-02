from datetime import date


def sorted_dates(dates):
    for i in sorted(map(lambda x: date.fromisoformat(x), dates)):
        print(i.strftime("%d/%m/%Y"))


sorted_dates(["2021-08-01", "2021-08-02", "2021-07-01", "2021-06-01", "2021-05-01"])
