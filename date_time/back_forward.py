from datetime import date, timedelta

s = date(*list(map(int, input().split(".")[::-1])))
print(
    (s - timedelta(days=1)).strftime("%d.%m.%Y"),
    (s + timedelta(days=1)).strftime("%d.%m.%Y"),
    sep="\n",
)
