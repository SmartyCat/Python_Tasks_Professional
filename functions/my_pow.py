def my_pow(number):
    number = str(number)
    return sum(int(item) ** index for index, item in enumerate(number, 1))

print(my_pow(139))
print(my_pow(123))