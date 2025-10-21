def power(degree):
    def func(x):
        return x**degree

    return func


square = power(2)
print(square(5))
print(power(3)(3))
result = power(4)(2)
print(result)
