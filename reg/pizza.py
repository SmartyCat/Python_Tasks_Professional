from re import findall, I

word, string = input(), input()

print(len(findall(rf"\b{word[:len(word)-2]}(se|ze)", string, flags=I)))
