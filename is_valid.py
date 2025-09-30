def is_valid(string):
    return 3 < len(string) < 7 and string.isdigit()

print(is_valid('4367'))
print(is_valid('92134'))
print(is_valid('89abc1'))
print(is_valid('900876'))
print(is_valid('49 83'))