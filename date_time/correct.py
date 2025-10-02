from datetime import date
from is_correct import is_correct

counter = 0
while True:
    s = input()
    if s == "end":
        break
    day, month, year = s.split(".")
    if is_correct(*map(int, (day, month, year))):
        print("Корректная")
        counter += 1
    else:
        print("Некорректная")
print(counter)
