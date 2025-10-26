def palindromes():
    n = 1
    while True:
        if str(n) == str(n)[::-1]:
            yield n
        n += 1

generator = palindromes()
numbers = [next(generator) for _ in range(30)]
print(*numbers)