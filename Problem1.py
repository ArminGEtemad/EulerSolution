# Problem 001: https://projecteuler.net/problem=1
# This problem is © Project Euler and used under CC BY-NC-SA 4.0
# Shared for educational, non-commercial purposes

# If we list all the natural numbers below 10
# that are multiples of 3 or 5, we get 
# 3, 5, 6, and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5
# below 1000.

limit = 1000
sum_multi = sum(i for i in range(1, limit) if i%3 == 0 or i%5 == 0)

print(f"{sum_multi = }")