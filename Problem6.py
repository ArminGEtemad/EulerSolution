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