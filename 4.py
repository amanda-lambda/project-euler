def is_palindrome(x):
    x = str(x)
    for i in range(len(x) // 2):
        if x[i] != x[-i-1]:
            return False
    return True

largest_palindrome = -1
for i in range(100,1000):
    for j in range(i,1000):
        x = i * j
        if is_palindrome(x):
            largest_palindrome = max(largest_palindrome, x)

print(largest_palindrome)
