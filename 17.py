import math

# Numbers less than 20
numbers = ["" for i in range(1001)]
numbers[1:21] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]

# Numbers less than 100
numbers[30], numbers[40], numbers[50], numbers[60], numbers[70], numbers[80], numbers[90] = "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
for i in range(21, 100):
    if not numbers[i]:
        numbers[i] = numbers[i//10*10] + numbers[i%10]

# Numbers less than 1000
for i in range(100, 1000):
    numbers[i] = numbers[i//100] + "hundred" 
    if i % 100:
        numbers[i] += "and" + numbers[i%100]

numbers[1000] = "onethousand"

print(sum([len(i) for i in numbers]))