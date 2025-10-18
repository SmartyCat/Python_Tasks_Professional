def to_binary(n):
    if n == 0:
        return "0"
    if n // 2 == 0:
        return "1"
    else:
        return "" + str(n % 2) + str(to_binary(n // 2))


print(to_binary(int(input()))[::-1])
