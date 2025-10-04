from datetime import datetime, time
from n import in_seconds

d = datetime.strptime(input(), "%d.%m.%Y %H:%M")
sec = in_seconds(d.time())
day_in, day_off = (time(9), time(21)), (time(10), time(18))
day_in, day_off = (
    (in_seconds(day_in[0]), in_seconds(day_in[1])),
    (in_seconds(day_off[0]), in_seconds(day_off[1])),
)

data = {0: day_in, 1: day_in, 2: day_in, 3: day_in, 4: day_in, 5: day_off, 6: day_off}
print(
    "Магазин не работает"
    if sec < data[d.date().weekday()][0] or sec > data[d.date().weekday()][1]
    else (data[d.date().weekday()][1] - sec) // 60
)
