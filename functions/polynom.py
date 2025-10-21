def polynom(x):
    result = x**2 + 1
    polynom.values.add(result)
    return result


polynom.__dict__["values"] = set()


for _ in range(10):
    polynom(10)
print(polynom.values)
