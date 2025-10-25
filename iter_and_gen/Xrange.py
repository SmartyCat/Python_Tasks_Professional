class Xrange:
    def __init__(self, start: int | float, end: int | float, step: int | float = 1):
        self.__start = start - step
        self.__end = end
        self.__step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.__step > 0:
            self.__start += self.__step
            if self.__start >= self.__end:
                raise StopIteration
        else:
            self.__start -= abs(self.__step)
            if self.__start <= self.__end:
                raise StopIteration
        return self.__start

xrange = Xrange(10, 1, -2)
print(*xrange)