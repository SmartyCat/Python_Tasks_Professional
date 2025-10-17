import calendar

try:
    s = int(input())
    try:
        print(calendar.month_name[s])
    except IndexError:
        print("Введено число из недопустимого диапазона")
except ValueError:
    print("Введено некорректное значение")
