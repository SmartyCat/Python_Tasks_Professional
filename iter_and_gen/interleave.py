interleave = lambda *args: (i for a in zip(*args) for i in a)

print(*interleave('bee', '123'))

numbers = [1, 2, 3]
squares = [1, 4, 9]
qubes = [1, 8, 27]
print(*interleave(numbers, squares, qubes))