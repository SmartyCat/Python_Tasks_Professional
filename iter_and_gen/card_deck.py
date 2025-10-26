def card_deck(suit):
    data = [
        j + " " + i
        for i in ("пик", "треф", "бубен", "червей")
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
        if suit not in i
    ]
    while True:
        for d in data:
            yield d


generator = card_deck("треф")
cards = [next(generator) for _ in range(40)]
print(*cards)
