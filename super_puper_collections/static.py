from collections import Counter

s = sorted(Counter([len(i) for i in input().split()]).items(), key=lambda x: x[1])
for length, count in s:
    print(f"Слов длинны {length}: {count}")
