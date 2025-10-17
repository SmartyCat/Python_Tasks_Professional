import json

try:
    with open(input(), encoding="utf-8") as file:
        try:
            print(json.load(file))
        except ValueError as e:
            print("Ошибка при десериализации")
except FileNotFoundError as e:
    print("Файл не найден")
