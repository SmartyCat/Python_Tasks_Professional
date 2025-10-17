def triangle(h):
    def func(n):
        if n <= h:
            print("*" * n)
            func(n + 1)

    func(1)


triangle(5)
