def print_given(*args, **kwargs):
    kwargs = dict(sorted(kwargs.items(), key=lambda x: x[0]))
    for a in args:
        print(a, type(a))
    for k in kwargs:
        print(k, kwargs[k], type(kwargs[k]))


print_given(1, [1, 2, 3], "three", two=2)
print_given("apple", "cherry", "watermelon")
print_given(b=2, d=4, c=3, a=1)
