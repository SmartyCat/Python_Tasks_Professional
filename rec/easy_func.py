def func(n=1):
    if n < 101:
        print(n)
        func(n + 1)


func()
