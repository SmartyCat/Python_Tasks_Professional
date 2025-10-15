from collections import Counter

s = Counter(input().lower().split())
min_char = s.most_common()[-1][1]
print(",".join(sorted(i[0] for i in s.most_common() if i[1] == min_char)))
