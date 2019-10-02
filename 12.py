import math

def find_divisors(x):
    divisors = []
    for i in range(1, math.ceil(math.sqrt(x))):
        if x % i == 0:
            divisors.append(i)
            if x // i != i:
                divisors.append(x//i)
    return divisors


curr_triangle_num = 1
curr_triangle_idx = 1

while True:
    curr_triangle_idx += 1
    curr_triangle_num += curr_triangle_idx
    divisors = find_divisors(curr_triangle_num)
    print(curr_triangle_num, len(divisors))
    if len(divisors) > 500:
        break

print(curr_triangle_num)