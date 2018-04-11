# Gareth Duffy 11-4-2018
# Old Faithful program (Topic 8 Ian)
# https://github.com/AM207/Site/blob/master/am207/content/files/oldfaithful.csv
# Use ipython, its better 
# Use TAB for completions of methods in ipython
# Use "run" in iPython
# Calculate the mean of each column
# 'nan' means "not a number"

import numpy
data = numpy.genfromtxt('data/faithful.csv', delimiter = ',')

# To print all of the values in a column you use the following:

firstcol = data [:,0] # First column # assigned to "firstcol" variable
secondcol = data [:,1] # Second column

meanfirstcol = numpy.mean(data [:,0]) # Print mean of column one 

print("The average of the first column is", meanfirstcol)

numpy.min(firstcol)
numpy.max(firstcol)

# Basic histogram for continous range of values
import matplotlib.pyplot as pl
pl.hist(firstcol) # 
pl.show()
