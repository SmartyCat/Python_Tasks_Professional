from collections import Counter

with open("/home/kostya/Загрузки/pythonzen.txt", encoding="utf-8") as file:
    rows = list(map(lambda x: list(x.strip().lower()), file.readlines()))
    counter = Counter()
    for row in rows:
        counter.update(row)
    for char in sorted(counter):
        if char.isalpha():
            print(f"{char}: {counter[char]}")
