from itertools import permutations

for i in sorted(set(permutations(input()))):
    print("".join(i))
