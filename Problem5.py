# Problem 005: https://projecteuler.net/problem=5
# This problem is © Project Euler and used under CC BY-NC-SA 4.0
# Shared for educational, non-commercial purposes

# 2520  is the smallest number that can be divided by 
# each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly
#  divisible by all of the numbers from  1 to 20 ?

from math import prod

def prime_facs_freq(N):
    i = 2
    prime_fac = []
    freq = {}
    while i * i <= N:
        if N % i == 0:
            prime_fac.append(i)
            N //= i
        else:
            i += 1
            
    if N > 1:
        prime_fac.append(N)
    
    for j in prime_fac:
        freq[j] = freq.get(j, 0) + 1

    return freq

def update_max_power(a, b):
    for prime, power in b.items():
        if prime in a:
            a[prime] = max(a[prime], power)
        else:
            a[prime] = power
    return a

results = {}
for i in range(2, 21):
    x = prime_facs_freq(i)
    update_max_power(results, x)

end_results = prod([prime_fac**power for prime_fac, power in results.items()])
print(f'smallest positive number that is evenly divisible by all of the numbers from  1 to 20 is {end_results}')