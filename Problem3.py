# Problem 003: https://projecteuler.net/problem=3
# This problem is © Project Euler and used under CC BY-NC-SA 4.0
# Shared for educational, non-commercial purposes

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

