def new_print(*args, sep=" ", end="\n"):
    old_print(
        *[a.upper() if isinstance(a, str) else a for a in args],
        sep=sep.upper(),
        end=end.upper()
    )


old_print = print
print = new_print
print("beegeek", [1, 2, 3], 4)
#print("bee", "geek", sep=" and ", end=" wow")
words = ("black", "white", "grey", "black-1", "white-1", "python")
print(*words, sep=" to ", end=" LOVE")
