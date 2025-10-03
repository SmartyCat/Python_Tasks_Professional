from datetime import datetime, timedelta

s = datetime.strptime(input(), "%d.%m.%Y")

for i in range(2, 12):
    print(s.strftime("%d.%m.%Y"))
    s += timedelta(days=i)
