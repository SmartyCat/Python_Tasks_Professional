from datetime import datetime

birthdays = {}
shablon = "%d.%m.%Y"
for i in range(int(input())):
    s = input().split()
    d = datetime.strptime(s[2], shablon).date()
    birthdays[d] = birthdays.get(d, []) + [s[0] + " " + s[1]]

old_date, name = min(birthdays.items(), key=lambda x: x[0])
old_date = datetime.strftime(old_date, shablon)
print(old_date + " " + name[0] if len(name) == 1 else old_date + " " + str(len(name)))
