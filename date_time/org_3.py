from datetime import datetime

shablon = "%d.%m.%Y"
check = datetime.strptime(input(), shablon).date()

birthdays = {}

for i in range(int(input())):
    s = input().split()
    d = datetime.strptime(s[2], shablon).date()
    if 0 < abs(check.day - d.day) <= 7 and check.month == d.month:
        birthdays[d] = " ".join(s[:2])
print(
    min(birthdays.items(), key=lambda x: x[0].day)[1]
    if birthdays
    else "Дни рождения не планируются"
)
