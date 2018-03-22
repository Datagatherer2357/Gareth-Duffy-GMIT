# Gareth Duffy 22-1-2018
# A program that displays Fibonacci numbers. (Excercise 1 Programming & Scripting)
# https://en.wikipedia.org/wiki/Fibonacci_number

#   """This function returns the nth Fibonacci number."""
def fib(n):
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x = 15
ans = fib(x)
print("Fibonacci number", x, "is", ans)


# My name is Gareth, so the first and last letter of my name (G + H = 7 + 8) give the number  15. The 15th Fibonacci number is 610.
