# What is the largest prime factor of 
# the number 600851475143?

n = 600851475143
i = 2

while i * i <= n:
    if n % i == 0:
        n //= i
    else:
        i += 1

print(f"Largest prime factor is {n}")

