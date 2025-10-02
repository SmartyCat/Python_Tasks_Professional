def transform_sequence(n, x, y, a, b):
    l = [i for i in range(1, n + 1)]
    l = l[: x - 1] + l[x - 1 : y][::-1] + l[y:]
    return l[:a-1]+l[a-1:b][::-1]+l[b:]


# Пример из условия
assert transform_sequence(9, 2, 5, 6, 9) == [1, 5, 4, 3, 2, 9, 8, 7, 6]

# Проверка, которую мы обсуждали
assert transform_sequence(5, 1, 3, 3, 5) == [3, 2, 5, 4, 1]

# Минимальный случай
assert transform_sequence(3, 1, 2, 2, 3) == [2, 3,1]

# Когда диапазоны перекрываются полностью
assert transform_sequence(6, 1, 6, 1, 6) == [1, 2, 3, 4, 5, 6]  # полностью переворачиваем дважды, вернётся к исходному

# Когда диапазоны перекрываются частично
assert transform_sequence(6, 2, 4, 3, 5) == [1, 4, 5, 2, 3, 6]

# Диапазоны касаются края последовательности
assert transform_sequence(7, 1, 3, 5, 7) == [3, 2, 1, 4, 7, 6, 5]