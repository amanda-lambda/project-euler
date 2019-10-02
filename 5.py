def is_prime(x):
    for i in range(2, math.ceil(x//2)):
        if x % i == 0:
            return False
    return True

def find_smallest_prime_factor(x):
    smallest_prime_factor = x
    for i in range(2, x):
        if x % i == 0:
            if is_prime(i):
                smallest_prime_factor = i
                break
    return smallest_prime_factor


def find_prime_factors(x):
    prime_factors = {}
    while x != 1:
        prime_factor = find_smallest_prime_factor(x)
        x = int(x / prime_factor)
        if prime_factor not in prime_factors:
            prime_factors[prime_factor] = 1
        else:
            prime_factors[prime_factor] += 1
    return prime_factors

minimal_prime_factors = {}
for i in range(2, 21):
    prime_factors = find_prime_factors(i)
    for f in prime_factors:
        if f in minimal_prime_factors:
            max_count = max(prime_factors[f], minimal_prime_factors[f])
            minimal_prime_factors[f] = max_count
        else:
            minimal_prime_factors[f] = prime_factors[f]

lcm = 1
for f in minimal_prime_factors:
    lcm *= f ** minimal_prime_factors[f]

print(lcm)