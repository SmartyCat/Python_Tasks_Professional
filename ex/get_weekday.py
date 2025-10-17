def get_weekday(number):
    days_of_week = [
        "Понедельник",
        "Вторник",
        "Среда",
        "Четверг",
        "Пятница",
        "Суббота",
        "Воскресенье",
    ]
    if not isinstance(number, int):
        raise TypeError("Аргумент не является целым числом")
    elif number not in (1, 2, 3, 4, 5, 6, 7):
        raise ValueError("Аргумент не принадлежит требуемому диапазону")
    return days_of_week[number - 1]


print(get_weekday(1))

try:
    print(get_weekday("hello"))
except Exception as err:
    print(err)
    print(type(err))

try:
    print(get_weekday(8))
except ValueError as err:
    print(err)
    print(type(err))
