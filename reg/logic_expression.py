from re import split

print(", ".join(split(r"\s*[\|\&]\s*|\s+and\s+|\s+or\s+", input())))
