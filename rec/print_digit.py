def print_digit(n):  # ПЕрвый способ решений
    if n > 0:
        print(n % 10)
        print_digit(n // 10)


def print_digit_2(s):  # Второй способ решения
    def func(n):
        if n > -1:
            print(str(s)[n])
            func(n - 1)

    func(len(str(s)) - 1)

print_digit(12345)
print_digit_2(12345)
