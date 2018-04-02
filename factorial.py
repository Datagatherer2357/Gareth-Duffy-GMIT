# Gareth Duffy 5-3-2018
# Factorial function algorithm (Excercise 6 Programming & Scripting)

# """ This function returns the factorial of any integer"""

def factorial(n): # function header 
  num = n # factorial input number value assigned to num variable
  for i in range(1, n): # for loop to iterate over all numbers less than factorial input number
      num = num * i # reassignment of num variable to multliply all looped numbers found with "i"
  return num # end of factorial function loop

print(factorial(5)) # Calling and printing of factorial function
print(factorial(7))
print(factorial(10))


#"""Version which asks for an integer at input and returns factorial statement"""

n = int(input("Please enter a number to show its factorial: "))

def factorial(n): # function header 
  num = n # factorial input number value assigned to num variable
  for i in range(1, n): # for loop to iterate over all numbers less than factorial input number
      num = num * i # reassignment of num variable to multliply all looped numbers found with "i"
  return num # end of factorial function loop

print("It's factorial is:", factorial(n), "!")
