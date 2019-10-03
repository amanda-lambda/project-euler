import math

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(x):
    if x % 100:
        if x % 400:
            return True
        else:
            return False
    if x % 4 == 0:
        return True
    return False

# Determine day of 1 Jan 1901
if is_leap_year(1900):
    start_day = sum(months_leap) % 7
else:
    start_day = sum(months) % 7 

# Number of first Sundays from 1901 to 2000
count = 0
for i in range(1901, 2001):
    for j in range(len(months)):
        if start_day == 0:
            count += 1
        start_day = (start_day + months[j]) % 7

print(count)
