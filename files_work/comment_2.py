import sys

print(*filter(lambda x: not x.lstrip().startswith("#"), sys.stdin.readlines()), sep="")
