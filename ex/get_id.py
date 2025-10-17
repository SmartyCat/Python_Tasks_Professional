def get_id(names, name):
    if not isinstance(name, str):
        raise TypeError("Имя не является строкой")
    elif not name[0].isupper() or (not name[1:].isalpha() or not name[1:].islower()):
        raise ValueError("Имя не является корректным")
    return len(names) + 1


names = ["Timur", "Anri", "Dima"]
name = "Arthur"
print(get_id(names, name))

names = ["Timur", "Anri", "Dima", "Arthur"]
name = "1Ruslan"
try:
    print(get_id(names, name))
except ValueError as e:
    print(e)

names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
name = ['E', 'd', 'u', 'a', 'r', 'd']
try:
    print(get_id(names, name))
except TypeError as e:
    print(e)