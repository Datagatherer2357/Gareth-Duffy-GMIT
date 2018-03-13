# Gareth Duffy 13-3-2018
# basic numpy WTOP

import numpy as np
x = np.arange(1, 10)
print(x)

print(x ** 2)

M = x.reshape((3, 3)) # multidimensional
print(M)

print(M.T) # transpose

print(np.dot(M, [5, 6, 7])) # matrix vector

print(np.linalg.eigvals(M)) # eigenvalues decompostion
