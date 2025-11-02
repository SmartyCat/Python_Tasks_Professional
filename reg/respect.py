from re import match, I

print(
    True
    if match(r"^(Здравствуйте|Доброе утро|Добрый день|Добрый вечер)", input(), flags=I)
    else False
)
