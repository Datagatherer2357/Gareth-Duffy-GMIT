# Gareth Duffy 27-4-2018
# OOP (Object Oriented Programming): Rectangles & classes.
# OOP is all turning big/complex "objects" into more succinctly packaged objects for ease of use.
# Classes are analogous to blueprints for a house build, in thus case houses "r1" and "r2" below.
# https://web.microsoftstream.com/video/5ec012bf-6910-41b9-a545-2b0660066e44
# https://docs.python.org/3/tutorial/classes.html
# https://python.swaroopch.com/oop.html

# r1x1 = 1 # rectangle coordinates (on plane)
# r1y1 = 3
# r1x2 = 5
# r1y2 = 6

# r2x1 = 3 # rectangle coordinates (on plane)
# r2y1 = 2
# r2x2 = 7
# r2y2 = 4

class Rectangle: # the class describes a type of object
    def __init__(self, x1, y1, x2, y2): # anything beginning and ending in 2 underscores like this is a special function #init = initialises !!!
        self.x1 = x1 # thus, r1.x1 below in fact become this "self.x1" variable
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

r1 = Rectangle(1, 3, 5, 6) # (House build No. 1) Values in these brackets get passed into the x1, y1 etc, variables in the init function.
r2 = Rectangle(3, 2, 7, 4) # (House build No.2)...Here, __init__ is being called.

print(r1.x1, r1.y1, r1.x2, r1.y2)
print(r2.x1, r2.y1, r2.x2, r2.y2)

# function to see if two rectangles overlap, returns a True answer if they do overlap (False if they don't).

def overlap(rectA, rectB):
    # adapted from :https://stackoverflow.com/a/306332/9324459
    if rectA.x1 < rectB.x2 and rectA.x2 > rectB.x1 and rectA.y2 > rectB.y1 and rectA.y1 < rectB.y2:
        return True
    else:
        return False

print(overlap(r1, r2))
