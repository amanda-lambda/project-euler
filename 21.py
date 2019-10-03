import math

def sum_proper_divisors(x):
    divisors = []
    for i in range(1, int(math.sqrt(x) + 1)):
        if x % i == 0:
            divisors.append(i)
            complement = x // i
            if (complement != i and complement != x):
                divisors.append(x//i)
    return sum(divisors)

sum_amicable_numbers = 0
list_of_sums = []
for i in range(10000):
    x = sum_proper_divisors(i)
    if x < i:
        if list_of_sums[x] == i:
            sum_amicable_numbers += x+i
    list_of_sums.append(x)

print(sum_amicable_numbers)
