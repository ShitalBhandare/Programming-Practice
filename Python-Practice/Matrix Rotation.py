

#python 3.5.2

# Matrix Rotation using numpy

import numpy as np

array = [[1,2,3],[4,5,6],[7,8,9]]
matrix = np.array(array)
print("Original Matrix:")
print(matrix)

print("Anticlock-wise 90 degree rotation:")
matrix = np.rot90(matrix, k=1)
print(matrix)

print("Anticlock-wise 180 degree rotation:")
matrix = np.rot90(matrix, k=2)
print(matrix)

print("Anticlock-wise 270 degree rotation:")
matrix = np.rot90(matrix, k=3)
print(matrix)

print("Clock-wise 90 degree rotation:")
matrix = np.rot90(matrix, k=4-1)
print(matrix)

