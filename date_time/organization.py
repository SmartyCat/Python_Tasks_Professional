from datetime import datetime
from functions import print_result

name, birthday = None, None
shablon = "%d.%m.%Y"
counter = 0
for i in range(int(input())):
    s = input().split()
    d = datetime.strptime(s[2], shablon).date()
    if name is None and birthday is None:
        name, birthday = s[0] + " " + s[1], d
        counter = 1
    elif d < birthday:
        name, birthday = s[0] + " " + s[1], d
        counter = 1
    elif birthday == d:
        counter += 1
print(print_result(name, birthday, counter))
