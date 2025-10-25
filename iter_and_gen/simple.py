def simple_sequence():
    n = 1
    while True:
        for _ in range(n):
            yield n
        n += 1


generator = simple_sequence()
numbers = [next(generator) for _ in range(10)]
print(*numbers)
