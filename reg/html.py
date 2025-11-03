from re import findall
import sys

for i in sys.stdin.readlines():
    result = findall(r'<a href="(.*)">(.*)</a>', i)
    if result:
        print(result[0][0], result[0][1], sep=", ")
