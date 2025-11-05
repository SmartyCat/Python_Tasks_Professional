from re import sub, findall
from string import punctuation

s = input()
result = []  # faster than string
data = findall(r"(\b\w+\W{0,})", s)  # make list of words

for index, item in enumerate(data):
    if index != len(data) - 1:
        first, second = "".join(i for i in item if i not in punctuation), "".join(
            i for i in data[index + 1] if i not in punctuation
        )  # remove punctuations
        if first.strip() != second.strip():
            result.append(item)
else:
    result.append(item)  # add last item
    print("".join(result))
