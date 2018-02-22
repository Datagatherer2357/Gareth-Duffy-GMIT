# Gareth Duffy 6-2-2018
# Fizzbuzz game!: https://en.wikipedia.org/wiki/Fizz_buzz

i = 1

while i <= 100: #Loop through the integers up to 100
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else: 
        print (i)
    i = i + 1