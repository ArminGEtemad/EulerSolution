# Problem 006: https://projecteuler.net/problem=10
# This problem is © Project Euler and used under CC BY-NC-SA 4.0
# Shared for educational, non-commercial purposes

# Find the sum of all the primes below two million

n = int(2e6)
list_of_all_nums = list(range(n))
cross_out_list = [True] * n
cross_out_list[0: 2] = [False, False] # 0 and 1 are not prime
p = 2

while p*p < n:
    if cross_out_list[p]:
        for i in range(p*p, n, p):
            cross_out_list[i] = False
    
    p += 1

primes = [i for i, is_prime in enumerate(cross_out_list) if is_prime]
print(sum(primes))