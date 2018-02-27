# Gareth Duffy 27-2-2018
# Iris excercise 5 
# Ronald Fisher's Iris dataset realligned with justification of spaces and columns

with open("data/iris.csv") as f:
  for line in f:
    data = line.split(',')  # Splits whitespace
    print('{0[0]:12} {0[1]:12} {0[2]:12} {0[3]:12} {0[4]:12}'.format(data))
