def is_prime(x):
    for i in range(2, math.ceil(x//2)):
        if x % i == 0:
            return False
    return True

i = 1
prime_count = 0
while prime_count <= 10001:
    i += 1
    if is_prime(i):
        prime_count += 1

print(i)