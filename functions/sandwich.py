def sandwich(func):
    def wrapper(*args, **kwargs):
        print("---- Верхний ломтик хлеба ----")
        result = func(*args, **kwargs)
        print("---- Нижний ломтик хлеба ----")
        if result is not None:
            return result

    return wrapper


@sandwich
def add_ingredients(ingredients):
    print(" | ".join(ingredients))


add_ingredients(["томат", "салат", "сыр", "бекон"])

print()


@sandwich
def beegeek():
    return "beegeek"


print(beegeek())
