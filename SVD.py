# Singular-value decomposition
from numpy import array
from scipy.linalg import svd
import math

# define a matrix
A = array([[math.sqrt(6)/2, -1], [math.sqrt(6)/2, 1]])
print(A)
# SVD
U, s, VT = svd(A)
print(U)
print(s)
print(VT)