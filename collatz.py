# Gareth Duffy 6-2-2018
# A program that demonstrates the Collatz conjecture sequence

x = int(input("Please enter a number to demonstrate the Collatz conjecture: "))

while x > 1:
    if x % 2 == 0:
        x = x / 2
        print (int(x))
    else:
        x = 3 * x + 1
        print (int(x))
    if x == 1:
        break
