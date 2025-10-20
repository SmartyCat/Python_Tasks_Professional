s = eval(input())

if isinstance(s, list):
    print(s[-1])
elif isinstance(s, tuple):
    print(s[0])
else:
    print(len(s))
