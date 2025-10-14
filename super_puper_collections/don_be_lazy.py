from collections import Counter

s = input().split(",")
result = sorted(Counter(s).items(), key=lambda x: x[0])

for name, count in result:
    print(f"{name}: {count}")
