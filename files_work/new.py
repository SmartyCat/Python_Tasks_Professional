import sys

data = list(map(lambda x: int(x.rstrip()), sys.stdin.readlines()))


def func(data):
    if not data:
        return ["нет учеников"]
    return [
        f"Рост самого низкого ученика: {min(data)}",
        f"Рост самого высокого ученика: {max(data)}",
        f"Средний рост: {sum(data)/len(data)}",
    ]


print(*func(data), sep="\n")
