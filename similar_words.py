def find_similar(word, words):
    words = list(map(lambda x: x.lower(), words))
    result = []
    word = word.lower()
    vowels = "уеыаоэияю"
    check = {
        len([i for i in word if i in vowels]): [
            index for index, item in enumerate(word) if item in vowels
        ]
    }
    for i in words:

        if {
            len([j for j in i if j in vowels]): [
                index for index, item in enumerate(i) if item in vowels
            ]
        } == check:
            result.append(i)
    return result
# слово: "молоко" → гласные на позициях 2,4,6
assert find_similar("молоко", ["корова", "тесто", "поле", "кокос"]) == ["корова"]

# слово: "тесто" → гласные на позициях 2,5
assert find_similar("тесто", ["место", "тесно", "свето", "тесто"]) == ["место", "тесно", "тесто"]

# слово: "книга" → гласные на позициях 2,5
assert find_similar("книга", ["книга", "книга", "книга"]) == ["книга", "книга", "книга"]

# слово: "компьютер" → гласные на позициях 2,4,7
assert find_similar("компьютер", ["копpьютер", "компотер", "компьютер"]) == ["копpьютер", "компьютер"]

# слово: "арбуз" → гласные на позициях 2,4
assert find_similar("арбуз", ["орбуз", "арбуз", "арбузик", "арбузо"]) == ["орбуз", "арбуз"]