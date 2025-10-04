from datetime import datetime

birthdays = {}
shablon = "%d.%m.%Y"

for i in range(int(input())):
    s = input().split()
    d = datetime.strptime(s[2], shablon).date()
    birthdays[d] = birthdays.get(d, []) + [s[0] + " " + s[1]]
maximum = len(max(birthdays.items(), key=lambda x: len(x[1]))[1])
birthdays = sorted(
    filter(lambda x: len(x[1]) == maximum, birthdays.items()), key=lambda x: x[0]
)
for i in birthdays:
    print(i[0].strftime(shablon))
