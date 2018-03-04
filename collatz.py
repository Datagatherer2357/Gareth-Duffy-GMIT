# Gareth Duffy 6-2-2018
# A program that demonstrates the Collatz conjecture sequence
# https://en.wikipedia.org/wiki/Collatz_conjecture

x = int(input("Please enter a number to demonstrate the Collatz sequence: "))

while x >= 1:  #  Specified starting value of 1 or higher.
    if x % 2 == 0:  # if loop that divides by 2 if number is even, and returns result.
        x = x / 2
        print (int(x))
    else:  # # else loop that multiplies by 3 if number is odd, and returns result.
        x = (x * 3) + 1
        print (int(x))
    if x == 1:  # if statement that terminates loop once the integer 1 is reached. 
        break
