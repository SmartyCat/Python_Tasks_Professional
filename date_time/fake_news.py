from datetime import datetime
from plural import choose_plural


def func(curent_date):
    shablon = "До выхода курса осталось:"
    curent_date = datetime.strptime(curent_date, "%d.%m.%Y %H:%M")
    constanta = datetime(2022, 11, 8, 12, 0)
    dif = constanta - curent_date
    dif_hours, dif_minutes = dif.seconds // 3600, (dif.seconds % 3600) // 60
    result_days, result_hours, result_minutes = (
        choose_plural(dif.days, ("день", "дня", "дней")),
        choose_plural(dif_hours, ("час", "часа", "часов")),
        choose_plural(dif_minutes, ("минута", "минуты", "минут")),
    )
    if dif.days > 0:
        return (
            f"{shablon} {result_days} и {result_hours}"
            if dif_hours != 0
            else f"{shablon} {result_days}"
        )
    elif dif.days == 0 and dif_hours != 0:
        return (
            f"{shablon} {result_hours} и {result_minutes}"
            if (dif.seconds % 3600) // 60 != 0
            else f"{shablon} {result_hours}"
        )
    elif dif_hours == 0:
        return f"{shablon} {result_minutes}"
    return "Курс уже вышел!"


print(func(input()))
