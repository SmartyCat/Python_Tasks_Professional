from datetime import date, timedelta


def dates(start: date, count: int = None):
    n = 0
    while n < count if count is not None else True:
        yield start + timedelta(days=n)
        n += 1


generator = dates(date(2022, 3, 8), 5)
print(*generator)
