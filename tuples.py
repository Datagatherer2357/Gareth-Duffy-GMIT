# Gareth Duffy 15-3-2018
# tuples (Udacity)

#1 

AngkorWat = (13.4125, 103.866667)
print(type(AngkorWat))

print("Angkor Wat is at latitude: {}".format(AngkorWat[0]))
print("Angkor Wat is at longitude: {}".format(AngkorWat[1]))

#2

dimensions = 52, 40, 100 
length, width, height = dimensions 
print("The dimensions are {}x{}x{}".format(length, width, height))

# In the second line, three variables are assigned from the content 
# of the tuple dimensions. This is called tuple unpacking. You can 
# use tuple unpacking to assign the information from a tuple into 
# multiple variables without having to access them one by one and make 
# multiple assignment statements. 

# There's also a place where the tuple's immutability is a perk. Unlike 
# lists, tuples can be stored in sets or used as the keys of a dictionary. 
# Since these two data structures require immutable keys, lists aren't 
# an option.

# 3
# In the example below we create a dictionary, world_heritage_locations 
# that has tuples of the form (latitude, longitude) as the keys and 
# strings denoting the corresponding place names as values:
world_heritage_locations = {(13.4125, 103.866667): "Angkor Wat",
                            (25.73333, 32.6): "Ancient Thebes",
                            (30.330556, 35.4433330): "Petra",
                            (-13.116667, -72.583333): "Machu Picchu"}

def first_and_last(sequence):
    """returns the first and last elements of a sequence"""
    return sequence[0], sequence[-1] # edit to see different outcomes

print(first_and_last(["genius", "idiot", "facist", "benevolent"]))








