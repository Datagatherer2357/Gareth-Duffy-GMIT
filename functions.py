# Gareth Duffy 5-3-2018
# making functions and algorithms week 7 

def sumall(upto):
  sumupto = 0 
  for i in range(1, upto + 1):
    sumupto = sumupto + i 
  return sumupto # output of function

print("The sum of the values from 1 to 50 inlusive is: ", sumall(50))


sum5 = 0
for i in range(1, 6):
  sum5 = sum5 + i 
print("The sum of the values from 1 to 5 inlusive is: ", sum5)


sum10 = 0
for i in range(1, 11):
  sum10 = sum10 + i 
print("The sum of the values from 1 to 10 inlusive is: ", sum10)

def gcd(x, y):
  while x != y:
    if x > y:
      x = x - y 
    else:
      y = y - x
  return x

def gcd(x, y):
  while x != 0 and y != 0:
    if x > y:
      x = x & y
    else:
      y = y % x
  if x == 0:
    return y
  else: 
    return x 
    
print("gcd of 6 and 15: ", gcd(6, 15))

z = gcd(221, 323)

print("gcd of 221 and 323: ", z)
