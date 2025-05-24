# Problem 002: https://projecteuler.net/problem=2
# This problem is © Project Euler and used under CC BY-NC-SA 4.0
# Shared for educational, non-commercial purposes

# Each new term in the Fibonacci sequence is generated 
# by adding the previous two terms. 
# By considering the terms in the Fibonacci sequence whose 
# values do not exceed four million, find the sum of 
# the even-valued terms.

a, b = 1, 2
sum_even_value = 0

while b <= 4e6:
    if b % 2 == 0:
        sum_even_value += b
    a, b = b, a + b

print(f"{sum_even_value = }")

