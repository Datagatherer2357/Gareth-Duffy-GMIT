# Gareth Duffy 25-2-2018
# function to calculate volume of a cylinder 

def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

volume = cylinder_volume(17, 12)
print(volume)