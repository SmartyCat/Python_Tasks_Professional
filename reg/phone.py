from re import search
import sys

data = sys.stdin.readlines()
for d in data:
    result = search(r"(\d{1,3})([- ])(\d{1,3})\2(\d{4,10}$)", d)
    print(
        f"Код страны: {result.group(1)}, Код города: {result.group(3)}, Номер: {result.group(4)}"
    )
