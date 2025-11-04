from re import sub


def normalize_whitespace(string: str) -> str:
    return sub(r" {2,}", r" ", string)


print(normalize_whitespace("""AAAA    A            AAA"""))

print(normalize_whitespace("Тут н   е            т лишних пробелов"))
