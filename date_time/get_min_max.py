from datetime import date


def get_min_max(dates):
    if not dates:
        return ()
    return min(dates), max(dates)


print(get_min_max([]))
