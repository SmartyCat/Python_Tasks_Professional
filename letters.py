def letters(a, b, c):
    en = "AaBCcEeHKMOoPpTXxy"
    ru = "АаВСсЕеНКМОоРрТХху"
    d = {True: "en", False: "ru"}
    default = any(map(lambda x: x in en, (a, b, c)))
    return "mix" if default and any(map(lambda x: x in ru, (a, b, c))) else d[default]


# Все три буквы английские
assert letters("A", "B", "C") == "en"
assert letters("x", "y", "T") == "en"

# Все три буквы русские
assert letters("А", "В", "С") == "ru"
assert letters("Х", "у", "Т") == "ru"

# Смесь русских и английских
assert letters("A", "В", "C") == "mix"
assert letters("x", "у", "T") == "mix"