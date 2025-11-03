from re import findall

s, word = input(), input()

print(len(findall(rf"\b{word}\b", s)))
