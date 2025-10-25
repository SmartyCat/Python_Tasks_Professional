class Fibonacci:
    def __init__(self):
        self.__n = 1
        self.__m = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.__n, self.__m = self.__m, self.__n + self.__m
        return self.__m
    
    
fibonacci = Fibonacci()
print(next(fibonacci))
print(next(fibonacci))