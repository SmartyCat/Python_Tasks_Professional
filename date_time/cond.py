from datetime import datetime, timedelta

left, right = (
    datetime.strptime(input(), "%d.%m.%Y").date(),
    datetime.strptime(input(), "%d.%m.%Y").date(),
)
for i in range((right - left).days):
    if (left.day + left.month) % 2 != 0:
        break
    left += timedelta(days=1)

while left <= right:
    if left.weekday() not in (0, 3):
        print(left.strftime("%d.%m.%Y"))
    left += timedelta(days=3)
