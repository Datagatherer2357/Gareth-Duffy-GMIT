# Gareth Duffy 22-1-2018
# A program that displays Fibonacci numbers. (Excercise 1 Programming & Scripting)
# https://en.wikipedia.org/wiki/Fibonacci_number

#"""This function returns the nth Fibonacci number.""" (Docstring)
# The point of functions is to take in inputs and return something.
def fib(n):
  i = 0
  j = 1
  n = n - 1

  while n >= 0: # while loop, condition that n is greater or equal to zero
    i, j = j, i + j
    n = n - 1
  
  return i # The return statement is used when a function is ready to exit and return a value back to 
           # its caller, without it, the function returns nothing 

# Test the fib function with the following value:
x = 15 # assigning the integer 15 to the new "x" variable
ans = fib(x) # calling fib function and assigning it to new "ans" variable
print("Fibonacci number", x, "is", ans)


# My name is Gareth, so the first and last letter of my name (G + H = 7 + 8) give the number  15. The 15th Fibonacci number is 610.
