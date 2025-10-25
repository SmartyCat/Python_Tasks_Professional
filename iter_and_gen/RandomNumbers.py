from random import randint


class RandomNumbers:
    def __init__(self, left: int, right: int, n: int):
        self.__left, self.__right, self.__n = left, right, n

    def __iter__(self):
        return self

    def __next__(self):
        if self.__n == 0:
            raise StopIteration
        self.__n -= 1
        return randint(self.__left, self.__right)

