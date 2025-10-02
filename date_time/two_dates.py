from datetime import date


def two_dates(start, end):
    return min(date.fromisoformat(start), date.fromisoformat(end)).strftime(
        "%d-%m (%Y)"
    )


start = "2021-05-12"
end = "2021-05-04"
print(two_dates(start, end))

start = "1999-07-14"
end = "1999-07-14"
print(two_dates(start, end))
