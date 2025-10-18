def count_numbers(n):
    if n < 10:
        return 1
    else:
        return 1 + count_numbers(n // 10)


print(count_numbers(int(input())))
