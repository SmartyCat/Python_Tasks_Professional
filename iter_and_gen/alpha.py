import string


class Alphabet:
    def __init__(self, language: str):
        self.__letters = (
            string.ascii_lowercase
            if language == "en"
            else "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        )
        self.__index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1
        if self.__index == len(self.__letters):
            self.__index = 0
        return self.__letters[self.__index]


en_alpha = Alphabet("en")
letters = [next(en_alpha) for _ in range(28)]
print(*letters)
