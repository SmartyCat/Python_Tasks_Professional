import sys

total_numbers = 0
elements = 0
for i in sys.stdin.readlines():
    try:
        total_numbers += float(i) if isinstance(i, float) else int(i)
    except ValueError:
        elements += 1

print(total_numbers, elements, sep="\n")
