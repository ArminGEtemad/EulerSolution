# Problem 001: https://projecteuler.net/problem=9
# This problem is © Project Euler and used under CC BY-NC-SA 4.0
# Shared for educational, non-commercial purposes

# There exists exactly one Pythagorean triplet for which 
# a + b + c = 1000
# findd a*b*c

# a^2 + b^2 = c^2
# a + b + c = 1000 
# c = 1000 - a - b
# c^2 = (1000 - a - b)^2
# a^2 + b^2 = (1000 - a - b)^2

for a in range(1000): # a cannot be greater than 1000
    for b in range(a+1, 1000-a): # a < b < c
        c = 1000 - a - b
        if a*a + b*b == c*c and a < c and b < c:
            print(f"{a=}, {b=}, {c=}")
            print(f"{a*b*c = }")