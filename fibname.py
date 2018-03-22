# Gareth Duffy 29-1-2018
# A program that displays Fibonacci numbers using people's names. (Excercise 2 Programming & Scripting)

# """Fibonacci function for names. This function returns the nth Fibonacci number""" (Docstring)

def fib(n):
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Duffy"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

# My surname is Duffy
# The first letter D is number 68
# The last letter y is number 121
# Fibonacci number 189 is 1409869790947669143312035591975596518914

# About the ord() function in Python:
# In very simple terms, ord() returns the ASCII value of a character. For example: ord (‘a’) returns the integer 97, while ord ('A') returns the integer 65. 
# It gives the opposite result of chr(), e.g. chr (97) is (‘a’).

# To explain:

# name = "Duffy" # (Assign the string to variable name)
# first = name[0] # (First letter of the string name)# last = name[-1] # (Last letter of the string name)
# firstno = ord(first) # (For my surname ord(D) converts to ASCII code 68)
# lastno = ord(last) # (For my surname ord(y) converts to ASCII code 121)
# x firstno + lastno # (x (Fibonacci number) is the sum of 68 + 121
