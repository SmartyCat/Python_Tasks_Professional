from collections import Counter

result = 0
data = Counter(input().split())

for i in range(int(input())):
    cl, price = input().split()
    if data[cl] > 0:
        result += int(price)
        data[cl] -= 1
print(result)
