# Gareth Duffy 16-4-2018
# exception error example

b = 3
c = 0

if c == 0:
    a = 1
else:
    a = (b/c)
print(a)

try:
    a = (b/c)
except:
    a = 1
print(a)

# try/except show youre preempting an error and show how you deal with it
#-----------------------------------------------------

b = 3
c = "abc"

try: 
    a = (b/c)
except ZeroDivisionError:
    a = 1
except TypeError:
    a = 2
except:
    a = 3
print(a)
