from re import search
import sys

for i in sys.stdin.readlines():
    result = search(r"^_\d{1,}[A-Za-z]*_?$", i)
    print(result is not None)