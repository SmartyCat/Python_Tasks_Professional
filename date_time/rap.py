from datetime import time, timedelta

start, end = input().split(":"), input().split(":")
start, end = (
    int(start[0]) * 3600 + int(start[1]) * 60,
    int(end[0]) * 3600 + int(end[1]) * 60,
)
x, start = start, start + 45 * 60
while True:
    if start > end:
        break
    print(
        time(hour=x // 3600, minute=(x % 3600) // 60).strftime("%H:%M")
        + " - "
        + time(hour=start // 3600, minute=(start % 3600) // 60).strftime("%H:%M")
    )

    x, start = start + 10 * 60, (start + 10 * 60) + 45 * 60
