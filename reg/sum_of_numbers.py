from re import compile, findall

a, b = input().split()
string = input()
regex = compile(r"\b\d+\b")
print(sum(int(i) for i in regex.findall(string, pos=int(a), endpos=int(b))))
