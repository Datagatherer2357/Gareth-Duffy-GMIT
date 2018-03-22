# Gareth Duffy 25-2-2018
# Euler project problem 5: Python program using for and range to calculate the smallest 
# positive number that is evenly divisible by all of the numbers from 1 to 20. (Excercise 4 Programming & Scripting).

# To find the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20, I discerned that I had to find 
# the lowest common multiple of these numbers. 
# After some thinking and research, I came to realise that any numbers which 
# are divisible by 11 to 20 are also divisible by 1 to 10. Therefore I chose to 
# omit integers 1 to 10 for parsimony.
# I then obtained formulas for lowest commom multiple (lcm), and for greatest 
# common divisor (gcd), because gcd was needed as part of the lcm formula. Thus, I
# would need to assign these formulas as functions in Python.

# gcd formula was extracted from https://codereview.stackexchange.com/questions/95521/gcd-using-euclid-algorithm
# lcm formula was extracted from https://www.math.nmsu.edu/~pmorandi/CourseMaterials/LCM

# I created the functions gcd, and lcm. I scripted gcd first in order to
# program Python to "understand" the lcm formula which would follow. 
# The lcm formula is based on finding the least commonn multiple of just two 
# numbers, so I had to create a for loop incorporating the range function in order
# to loop over all numbers in the 11 to 20 range.

# The result (eul5) was checked using https://www.calculatorsoup.com/calculators/math/lcm.php

print("What is the the smallest positive number evenly divisible by all numbers from 1 to 20?")

#"""This function returns the greatest common divisor of two natural numbers"""
def gcd(a, b): 
  while b:
    a, b = b, a % b
  return a

#"""This function returns the lowest common multiple of two natural numbers"""
def lcm(a, b):  
  return (a * b) / gcd(a, b)

eul5 = lcm(11, 20)  # lcm function assigned to eul5 (solution) variable. Finds the lcm of 11 and 20.
for i in range(11, 21): # for loop using "i" variable to iterate over all integers ranging 11-20.
  eul5 = lcm(eul5, i) # argument of lcm function updated to yield smallest positive number of all integers
                      # integers ranging 11 to 20. Line of code (altered) was taken from: https://gist.github.com/PEZ   

print("The smallest positive number is", int(eul5)) 

