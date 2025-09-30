def same_parity(numbers):
    if not numbers:
        return []
    parity = numbers[0] % 2
    return [i for i in numbers if i % 2 == parity]

print(same_parity([1,2,3,4,5]))
