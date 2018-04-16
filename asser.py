# Gareth Duffy 16-4-2018
# raising and asserting
# factorial function 

def fac(n):
    if n < 0:
        raise ValueError # or depending on situation use instead: assert n >= 0
    ans = 1

    while n > 0:
        ans = ans * n
        n = n -1
    return ans

for i in range(-10, 10):
    try: 
        print(i, "factorial is", fac(i))
    except ValueError:
        print(i, "is negative value undefined")

# assert and raise are very similar apart from the situation they are used in 
# assert checks for a true/false condition, if it ends up being false an assertion error is raised
# raise wont crash your program like assert, and you can deal with it unlike assert.
