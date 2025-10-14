from collections import defaultdict


def wins(pairs):
    result = defaultdict(set)
    for winner, loser in pairs:
        result[winner].add(loser)
    return result


result = wins([("Тимур", "Артур"), ("Тимур", "Дима"), ("Дима", "Артур")])
for winner, losers in sorted(result.items()):
    print(winner, "->", *sorted(losers))

result = wins(
    [("Артур", "Дима"), ("Артур", "Тимур"), ("Артур", "Анри"), ("Дима", "Артур")]
)
for winner, losers in sorted(result.items()):
    print(winner, "->", *sorted(losers))
