from collections import Counter


def print_bar_chart(data, mark):
    data = Counter(data)
    space = len(max(data, key=len))
    for d in sorted(data.items(), key=lambda x: x[1], reverse=True):
        print(d[0] + " " * (space - len(d[0]) + 1) + "|", mark * d[1])


print_bar_chart("beegeek", "+")
languages = [
    "java",
    "java",
    "python",
    "C++",
    "assembler",
    "java",
    "C++",
    "C",
    "pascal",
    "C++",
    "pascal",
    "java",
]
print_bar_chart(languages, "#")
