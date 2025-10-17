try:
    with open(input(), encoding="utf-8") as file:
        for line in file:
            print(line.rstrip())
except FileNotFoundError:
    print("Файл не найден")
