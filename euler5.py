# Gareth Duffy 20-2-2018
# Euler project problem 5: Python program using for and range to calculate the smallest 
# positive number that is evenly divisible by all of the numbers from 1 to 20

# To find the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20, I realized that I had to find 
# the lowest common multiple of these numbers. 

# Importantly, I then came to realise that any numbers which are divisible by 
# 11 to 20 are similarly divisible by 1 to 10, therefore, for parsimony, 
# I omitted integers 1 to 10.

# I then searched for the formulas of lowest commom multiple (lcm) and also greatest 
# common divisor (gcd), because gcd is needed as part of the lcm formula. Thus, I
# would need to assign these formulas as functions in Python.

# gcd formula was extracted from https://codereview.stackexchange.com/questions/95521/gcd-using-euclid-algorithm
# lcm formula was extracted from https://www.math.nmsu.edu/~pmorandi/CourseMaterials/LCM

# I then created the functions gcd, and lcm. I created gcd first in order to
# program Python to understand the lcm formula which would follow it. 

# result (e5) checked using https://www.calculatorsoup.com/calculators/math/lcm.php

def gcd(a, b):  # Function of greatest common divisor formula
  while b:
    a, b = b, a % b
  return a

def lcm(a, b):  # Function of lowest common multiple formula
  return (a * b) / gcd(a, b)

e5 = lcm(11, 21)  # e5 (problem solution) variable assigned to adhere to lcm formula
for i in range(11, 21): # for loop created using "i" variable to iterate over integers ranging 11-20
  e5 = lcm(i, e5)  # lcm formula loop with i variable to generate smallest positive number solution

print(e5)