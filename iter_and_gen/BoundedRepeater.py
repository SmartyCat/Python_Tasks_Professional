class BoundedRepeater:
    def __init__(self, obj, times):
        self.__obj = obj
        self.__times = times

    def __iter__(self):
        return self

    def __next__(self):
        if self.__times == 0:
            raise StopIteration
        self.__times -= 1
        return self.__obj


geek = BoundedRepeater("geek", 3)
print(next(geek))
print(next(geek))
print(next(geek))
try:
    print(next(geek))
except StopIteration:
    print("Error")
