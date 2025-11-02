from re import search
import sys

for i in sys.stdin.readlines():
    i = i.rstrip()
    midl = len(i) // 2
    result = search(r"(\w+)\1{1,}", i)
    if i[:midl] == i[midl:] and result is not None:
        print(result.group())
