from itertools import groupby

s = groupby(sorted(input().split(),key=lambda x: (len(x),x)),key=len)

for i in s:
    print(f"{i[0]} -> {', '.join(i[1])}")