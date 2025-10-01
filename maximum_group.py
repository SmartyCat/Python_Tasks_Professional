from functools import reduce


def max_group(n):
    d = {}
    for i in range(1, n + 1):
        sum_numbers = reduce(lambda x, y: x + int(y), str(i), 0)
        d[sum_numbers] = d.get(sum_numbers, 0) + 1
    return max(d.values())


# n = 1 → группы: (1) → макс. длина = 1
assert max_group(1) == 1

# n = 2 → группы: (1), (2) → макс. длина = 1
assert max_group(2) == 1

# n = 10 → группы: (1,10), (2), ... (9) → макс. длина = 2
assert max_group(10) == 2

# n = 20 → пример из условия → макс. длина = 3
assert max_group(20) == 3

# n = 30 → макс. длина = 4 (сумма цифр=3 → 3, 12, 21, 30)
assert max_group(30) == 4

# n = 100 → макс. длина = 10 (группа с суммой цифр=9)
assert max_group(100) == 10
