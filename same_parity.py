def same_parity(numbers):
    return [] if not numbers else [i for i in numbers if i % 2 == numbers[0] % 2]


print(same_parity([1, 2, 3, 4, 5]))
