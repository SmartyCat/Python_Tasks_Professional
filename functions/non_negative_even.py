def non_negative_even(numbers):
    return all(map(lambda x: x % 2 == 0 and x >= 0, numbers))


print(non_negative_even([1, 2, 4, 8, 16]))
print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))