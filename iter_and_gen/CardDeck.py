class CardDeck:
    def __init__(self):
        self.__number = -1
        self.__data = [
            j + " " + i
            for i in ("пик", "треф", "бубен", "червы")
            for j in (
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "валет",
                "дама",
                "король",
                "туз",
            )
        ]

    def __iter__(self):
        return self

    def __next__(self):
        self.__number += 1
        if self.__number == 52:
            raise StopIteration
        return self.__data[self.__number]


cards = list(CardDeck())
print(cards[9])
print(cards[23])
print(cards[37])
print(cards[51])
