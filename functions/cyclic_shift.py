def cyclic_shift(numbers: list[int | float], step: int) -> None:
    for _ in range(abs(step)):
        item = (
            numbers.pop(0) if step < 0 else numbers.pop()
        )  # решил поэексперементировать с тернарным оператором
        (
            numbers.append(item) if step < 0 else numbers.insert(0, item)
        )  # мне кажеться так лучше


numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, 1)
print(numbers)
numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, -7)
print(numbers)
