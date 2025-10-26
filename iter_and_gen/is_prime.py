is_prime = lambda n: n > 1 and all(
    True if n % i != 0 else False for i in range(2, int(n**0.5) + 1)
)

print(is_prime(11))
print(is_prime(8))
print(is_prime(1))
