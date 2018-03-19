# Gareth Duffy 2-3-2018
# while loop with break statement for fibonacci sequence 
# up to a specified number (amax)
# p40 WTO Python 

a, b = 0, 1
amax = 400
L = []
while True:
  (a, b) = (b, a + b)
  if a > amax:
    break
  L.append(a)
print(L)

# Note that the while True loop will loop forever 
# unless we use a break statement
