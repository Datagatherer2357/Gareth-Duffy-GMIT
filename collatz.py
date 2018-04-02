# Gareth Duffy 6-2-2018
# A program that demonstrates the Collatz conjecture sequence. (Excercise 3 Programming & Scripting).
# https://en.wikipedia.org/wiki/Collatz_conjecture

x = int(input("Please enter a number to demonstrate the Collatz sequence: ")) # input function request assigned to variable "x"

while x >= 1:  #  while loop that specifies a starting value of 1 or higher.
    if x % 2 == 0:  # if statement/condition that divides by 2 if number is even, and returns result.
        x = x / 2 # x is now x divided by 2
        print (int(x))
    else:  # # else statement that multiplies by 3 if number is odd, and returns result.
        x = (x * 3) + 1 # x is equal itself multiplied by 3
        print (int(x))
    if x == 1:  # if statement that terminates loop once the integer 1 is reached. 
        break # stop while loop 
