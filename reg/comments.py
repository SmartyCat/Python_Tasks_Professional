import sys
from re import sub

s = ''
result = []
for i in sys.stdin.readlines():
    if "#" in i:
        result.append(i[: i.index("#")].rstrip() + "\n")
    elif '"""' in i or '"""' in s:
        s += i
        if s.count('"')==6:
            s = ''
    else:
        result.append(i)
else:
    result[-1] = result[-1].rstrip()
    print("".join(result))
