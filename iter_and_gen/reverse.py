def reverse(sequence):
    yield from reversed(sequence)


print(*reverse([1, 2, 3, 4, 5]))

generator = reverse("beegeek")
print(type(generator))
print(*generator)
