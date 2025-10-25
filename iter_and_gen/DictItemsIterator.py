class DictItemsIterator:
    def __init__(self, data: dict):
        self.__index = -1
        self.__list = list(data)
        self.__data = data

    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1
        if self.__index == len(self.__data):
            raise StopIteration
        return self.__list[self.__index], self.__data[self.__list[self.__index]]

pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})
print(*pairs)

data = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
pairs = DictItemsIterator(data)
print(*pairs)