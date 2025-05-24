# Problem 006: https://projecteuler.net/problem=6
# This problem is © Project Euler and used under CC BY-NC-SA 4.0
# Shared for educational, non-commercial purposes

# Find the difference between the sum of the squares of the 
# first one hundred natural numbers and the square of the sum.

def sum_of_squares(N):
    y = [x*x for x in range(N+1)]
    return sum(y)

def suqare_of_sums(N):
    y = sum([x for x in range(N+1)])
    return y*y

result = suqare_of_sums(100) - sum_of_squares(100)
print(result)