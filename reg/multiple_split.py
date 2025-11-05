from re import split, escape


def multiple_split(string: str, delimiters: list) -> str:
    regex = "|".join(map(escape, delimiters))
    return split(regex,string)

print(multiple_split("beegeek-python.stepik", [".", "-"]))

print(multiple_split("Timur---Arthur+++Dima****Anri", ["---", "+++", "****"]))

print(multiple_split("timur.^[+arthur.^[+dima.^[+anri.^[+roma.^[+ruslan", [".^[+"]))
print(multiple_split("hello and world", ["and"]))
