import sys

total_numbers = 0
elements = 0
for i in sys.stdin.readlines():
    try:
        i = float(i) if "." in i else int(i)
        total_numbers += i
    except ValueError:
        elements += 1

print(total_numbers, elements, sep="\n")
