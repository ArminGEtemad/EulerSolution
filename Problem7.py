# Problem 006: https://projecteuler.net/problem=7
# This problem is © Project Euler and used under CC BY-NC-SA 4.0
# Shared for educational, non-commercial purposes

# what is the 10001st prime number?

n = 10001
prime_list = [2]

while len(prime_list) < n:
    last_element = max(prime_list)
    next_num = last_element + 1
    while any(next_num % element == 0 for element in prime_list):
        next_num += 1
    prime_list.append(next_num)


print(max(prime_list))

