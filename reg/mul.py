from re import sub

s = input()
while "(" in s:
    s = sub(r"(\d+)\((\w+)\)", lambda x: int(x.group(1)) * x.group(2), s)
else:
    print(s)
