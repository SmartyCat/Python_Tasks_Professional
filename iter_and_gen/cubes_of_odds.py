cubes_of_odds = lambda l: (i**3 for i in l if i % 2 != 0)  # в одну строку
print(*cubes_of_odds([1, 2, 3, 4, 5]))
evens = [2, 4, 6, 8, 10]
print(list(cubes_of_odds(evens)))