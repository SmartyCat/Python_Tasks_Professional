from re import findall

s, word = input(), input()

print(len(findall(rf"\w+{word}\w+", s)))
