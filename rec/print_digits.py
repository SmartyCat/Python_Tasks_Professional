def print_digits(n):
    s = str(n)
    def func(number):
        if number < len(s):
            print(s[number])
            func(number + 1)

    func(0)


print_digits(12345)
