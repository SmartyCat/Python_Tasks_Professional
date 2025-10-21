def sort_priority(values, group):
    result = sorted(i for i in values if i in group) + sorted(
        i for i in values if i not in group
    )
    for index, item in enumerate(result):
        values[index] = item


numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
sort_priority(numbers, (300, 100, 200))
print(numbers)
