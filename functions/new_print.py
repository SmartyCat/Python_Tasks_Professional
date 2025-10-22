def dec(func):
    def wrapper(*args, sep=" ", end="\n"):
        func(*[str(a).upper() for a in args], sep=sep.upper(), end=end.upper())

    return wrapper


print = dec(print)

print("hi", "there", end="!")
print("are you in trouble?")
print(111, 222, 333, sep="xxx")
