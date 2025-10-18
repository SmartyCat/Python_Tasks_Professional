def is_power(n):
    if n == 1:
        return True
    elif n % 2 == 0:
        return is_power(n // 2)
    return False


print(is_power(8))
