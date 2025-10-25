class Cycle:
    def __init__(self, iterable):
        self.__iterable = iterable
        self.__index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1
        if self.__index == len(self.__iterable):
            self.__index = 0
        return self.__iterable[self.__index]
