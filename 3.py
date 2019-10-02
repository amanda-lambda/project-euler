x = 600851475143 

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


largest_prime_factor = 1
while x != 1:
    prime_factor = find_smallest_prime_factor(x)
    largest_prime_factor = max(prime_factor, largest_prime_factor)
    x = int(x / prime_factor)

print(largest_prime_factor)