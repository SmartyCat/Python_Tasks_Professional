from datetime import datetime
from is_correct import is_correct, trans

with open("diary.txt", "r", encoding="utf-8") as file:
    l = file.readlines()
    d = {}

    for i in l:
        if is_correct(i.rstrip()):
            key = trans(i.rstrip())
            d[key] = ""
        else:
            d[key] += i

for i in sorted(d.items(), key=lambda x: x[0]):
    print(i[0].strftime("%d.%m.%Y; %H:%M"), i[1],sep="\n")
