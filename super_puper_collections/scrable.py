from collections import Counter


def scrabble(symbols, word):
    d1, d2 = Counter(symbols), Counter(word.lower())
    for d in d2:
        if d1[d] < d2[d]:
            return False
    return True


print(scrabble("bbbbbeeeeegggggggeeeeeekkkkk", "Beegeek"))
print(scrabble("begk", "beegeek"))
print(scrabble("beegeek", "beegeek"))
