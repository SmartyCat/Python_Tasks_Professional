from itertools import permutations


def get_biggest(numbers):
    if not numbers:
        return -1
    numbers = [str(i) for i in numbers]
    return max([int("".join(i)) for i in permutations(numbers)])


print(get_biggest([2, 1, 3]))
print(get_biggest([61, 228, 9, 3, 11]))
print(get_biggest([7, 71, 72]))
