def find_duplicates(s):
    d = {}
    for i in s.split():
        d[int(i)] = d.get(int(i), 0) + 1
    return " ".join(
        map(
            lambda x: str(x[0]),
            sorted(filter(lambda x: x[1] > 1, d.items()), key=lambda x: x[0]),
        )
    )


# тест с повторяющимися числами
assert find_duplicates("1 2 3 2 4 5 1") == "1 2"

# тест с одним повторяющимся числом
assert find_duplicates("7 8 9 7") == "7"

# тест без повторов
assert find_duplicates("1 2 3 4 5") == ""

# тест с повторяющимися числами подряд
assert find_duplicates("5 5 5 6 6") == "5 6"

# тест с большим числом элементов
assert find_duplicates("10 20 10 30 40 20 50 10") == "10 20"