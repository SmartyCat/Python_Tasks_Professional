from collections import Counter

data = sorted(Counter(input().split(",")).items())
max_len = len(max(data, key=lambda x: len(x[0]))[0])
for product, count in data:
    sum_of_chars = sum(ord(i) for i in product)
    space = " " * (max_len - len(product))
    print(
        product + space + ":", f"{sum_of_chars} UC x {count} = {sum_of_chars*count} UC"
    )
