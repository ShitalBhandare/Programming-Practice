
# Numpy Basic operations program

# Numpy usage program in Python

import numpy as np

arr = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

#print(arr)
    
# Slicing
temp = arr[1:, ::2]
print(temp)

# Integer array indexing
temp = arr[[2,1],[0,2]]
print(temp)

# Boolean array indexing
cond = arr > 3
temp = arr[cond]
print(temp)

# Basic Operations: + - * /
arr = np.array([1,2,3,4])
print(arr*2)

# Transpose of the array
arr = np.array([[1,2,3],[4,5,6]])
print(arr.T)

# Unary Operations:
print(arr.sum())

# axis = 0: column
# axis = 1: Row

# Column wise max
print(arr.max(axis = 0))

# Row wise max
print(arr.max(axis = 1))

arr2 = np.array([[7,8,9],[2,4,5]])

# Element wise multiplication
print(arr*arr2)

# Matrix multiplication
#print(arr.dot(arr2))


Output:

Python 3.6.1 (default, Dec 2015, 13:05:11)
[GCC 4.8.2] on linux
[[4 6]
 [7 9]]
[7 6]
[4 5 6 7 8 9]
[2 4 6 8]
[[1 4]
 [2 5]
 [3 6]]
21
[4 5 6]
[3 6]
[[ 7 16 27]
 [ 8 20 30]]


