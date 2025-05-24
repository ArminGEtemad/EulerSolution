# Problem 004: https://projecteuler.net/problem=4
# This problem is © Project Euler and used under CC BY-NC-SA 4.0
# Shared for educational, non-commercial purposes

# A palindromic number reads the same both ways. 
# The largest palindrome made from the product 
# of two 2-digit numbers is 9009 = 91 x 99
# What is the largest palindrome made from the
# product of two 3-digit numbers

init = 100
final = 999
max_palindrome = 0
for i in range(final, init, -1):
    for j in range(i, init, -1):
        num = i*j
        if num <= max_palindrome:
            break
        num_str = str(i*j)
        num_str_reversed = num_str[::-1]
        if num_str == num_str_reversed:
            max_palindrome = int(num_str)
print(max_palindrome)