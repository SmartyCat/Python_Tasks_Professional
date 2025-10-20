def convert(number):
    b, o, h = bin(number)[2:], oct(number)[2:], hex(number).upper()[2:]
    return (b, o, h) if number > 0 else ("-" + b, "-" + o, "-" + h)


print(convert(15))
print(convert(-24))
print(convert(1))
