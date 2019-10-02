def is_prime(x):
    for i in range(2, math.ceil(x//2)):
        if x % i == 0:
            return False
    return True

sum = 0
for i in range(2, 2000000):
    if is_prime(i):
        print(i)
        sum += i

print(sum)