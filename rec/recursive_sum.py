def recursive_sum(a, b):
    if b != 0:
        return 1 + recursive_sum(a, b - 1)
    elif a != 0:
        return 1 + recursive_sum(a - 1, 0)
    else:
        return 0


print(recursive_sum(45,35))
