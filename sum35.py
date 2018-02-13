# Gareth Duffy 13-2-2018
# Project Euler problem 1

sum = 0
i = 1

while i < 1000:
    if i % 3 == 0:
        sum = sum + i
    elif i % 5 == 0:
        sum = sum + i
    i = i + 1

print ("sum of multiples 3 and 5, less than 1000", sum)