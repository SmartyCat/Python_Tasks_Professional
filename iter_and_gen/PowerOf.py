class PowerOf:
    def __init__(self, number: int):
        self.__number = number
        self.__pow = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__pow += 1
        return self.__number**self.__pow
    
    
power_of_two = PowerOf(2)
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))