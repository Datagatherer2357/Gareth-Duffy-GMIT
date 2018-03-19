# Gareth Duffy 14-3-2018
# Ian's 10 practice example problems on Moodle

# problem 1 
# function sumultiply that takes two integer 
# arguments and returns their product

def sumultiply(x, y):
    
  total = 0 # keep track of total, set to 0 at start

  for i in range(y): # loops and returns all values up to but not including y
    total = total + x # add x to total each time we loop 

  return total

print(sumultiply(11, 13))
print(sumultiply(5, 123))

# problem 2
# palindrome program  takes a string and returns True 
# if the string is a palindrome and False otherwise

def ispalindrome(s):
  ans = True  # final result

  for i in range(len(s)): # loop through one character at a time
    if s[i] != s[len(s)-1-i]: # compare first character to last etc
        ans = False
  return ans # return the answer 

print(ispalindrome("rotator"))
print(ispalindrome("rotators"))
