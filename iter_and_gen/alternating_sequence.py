def alternating_sequence(count: int = None):
    n = 1
    while n <= count if count is not None else True:
        yield n if n % 2 != 0 else -n
        n += 1

generator = alternating_sequence()
print(next(generator))
print(next(generator))

generator = alternating_sequence(10)
print(*generator)