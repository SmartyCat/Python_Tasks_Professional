from datetime import date


def is_correct(day, month, year):
    try:
        date(year, month, day)
        return True
    except:
        return False
