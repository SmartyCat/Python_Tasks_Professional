from re import findall, I

word, string = input(), input()

print(len(findall(rf"\b{word[:-3]}(or|our)\b", string, flags=I)))
