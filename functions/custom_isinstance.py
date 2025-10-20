def custom_isinstance(objects, typeinfo):
    return sum(isinstance(o, typeinfo) for o in objects)


numbers = [1, "two", 3.0, "четыре", 5, 6.0]
print(custom_isinstance(numbers, int))
numbers = [1, "two", 3.0, "четыре", 5, 6.0]
print(custom_isinstance(numbers, (int, float)))
numbers = [1, "two", 3.0, "четыре", 5, 6.0]
print(custom_isinstance(numbers, list))
