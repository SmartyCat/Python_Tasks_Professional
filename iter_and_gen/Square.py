class Square:
    def __init__(self, n: int):
        self.__n = n
        self.__square = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__n == 0:
            raise StopIteration
        self.__n -= 1
        self.__square += 1
        return self.__square**2
