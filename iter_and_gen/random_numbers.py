from random import randint


def random_numbers(left: int, right: int):
    return iter(lambda: randint(left, right), right + 1)

