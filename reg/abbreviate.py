from re import findall


# the first basic solution
def abbreviate(phrase):
    result = []
    for p in phrase.split():
        result.append(p[0].upper())
        for i in p[1:]:
            if i.isupper():
                result.append(i)
    else:
        return "".join(result)


# the second solution with regular
def abbreviate(phrase):
    return "".join(
        i.upper() for i in findall(r"([A-Z]?|\b.)", phrase) if not i.isspace()
    )


print(abbreviate("javaScript object notation"))

print(abbreviate("frequently asked questions"))

print(abbreviate("JS game sec"))
