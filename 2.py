curr = 1
next = 2
sum_even_terms = 0

while curr < 4000000:
    next_copy = next
    next = curr + next_copy
    curr = next_copy
    if curr % 2 == 0:
        sum_even_terms += curr

print(sum_even_terms)