
# Numpy usage program in Python

import numpy as np

arr = np.array([[1,2,3],
              [4,5,6]])

print(arr)
    
print("Type of array:", type(arr))
print("Dimention of array:", arr.ndim)
print("Shape of array:", arr.shape)
print("Size of the array:", arr.size)
print("Elements type in array:", arr.dtype)

print("************************")

arr1 = np.array([[1,2,3], [4,5,6]], dtype='float')
print("\narr1:\n", arr1)

arr2=np.array((1,2,3))
print("\narr2:\n",arr2)

arr3 = np.full((2, 3),4, dtype='complex')
print("\narr3:\n",arr3)

arr4 = np.random.random((2,2))
print("\narr4:\n",arr4)

arr5 = np.arange(0,30,5)
print("\narr5:\n",arr5)

arr6 = np.linspace(0,2,7)
print("\narr6:\n",arr6)

arr7 = arr.reshape((3,2))
print("\narr7:\n",arr7)

arr8 = arr7.flatten()
print("\narr8:\n",arr8)

Output:

Python 3.6.1 (default, Dec 2015, 13:05:11)
[GCC 4.8.2] on linux
[[1 2 3]
 [4 5 6]]
Type of array: <class 'numpy.ndarray'>
Dimention of array: 2
Shape of array: (2, 3)
Size of the array: 6
Elements type in array: int64
************************

arr1:
 [[1. 2. 3.]
 [4. 5. 6.]]

arr2:
 [1 2 3]

arr3:
 [[4.+0.j 4.+0.j 4.+0.j]
 [4.+0.j 4.+0.j 4.+0.j]]

arr4:
 [[0.66271701 0.31087368]
 [0.0384643  0.66619373]]

arr5:
 [ 0  5 10 15 20 25]

arr6:
 [0.         0.33333333 0.66666667 1.         1.33333333 1.66666667
 2.        ]

arr7:
 [[1 2]
 [3 4]
 [5 6]]

arr8:
 [1 2 3 4 5 6]

