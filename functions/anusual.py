s = list(input())

print(
    "".join(
        sorted(filter(lambda x: x.islower(), s))
        + sorted(filter(lambda x: x.isupper(), s))
        + sorted(filter(lambda x: x.isdigit() and int(x) % 2 != 0, s))
        + sorted(filter(lambda x: x.isdigit() and int(x) % 2 == 0, s))
    )
)
