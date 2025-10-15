from collections import Counter

s = Counter(input().lower().split())
max_char = s.most_common()[0][1]
print(max(i[0] for i in s.most_common() if i[1] == max_char))
