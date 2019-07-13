

import numpy as np
a = np.array([0, np.pi/2, np.pi])

print(a)
print(np.sin(a))

a = np.array([0,1,2,3])
print(a)
print(np.exp(a))

print(np.sqrt(a))


# Sorting of array

a = np.array([[1,4,2],[3,2,0]])
print(a)

# By default row wise sorting
print(np.sort(a))

# Axis = 1 means row wise
print(np.sort(a, axis=1))

# Axis = 0 means column wise
print(np.sort(a, axis=0, kind='mergesort'))

dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]
values= [('shital', 2016, 9.0),('dipa', 2016, 8.5), ('priya', 2015, 7.0)]

a = np.array(values, dtype = dtypes)

a= np.sort(a, order='name')
print(a)

print(np.sort(a, order=['grad_year', 'cgpa']))



Output:

Python 3.6.1 (default, Dec 2015, 13:05:11)
[GCC 4.8.2] on linux
[0.         1.57079633 3.14159265]
[0.0000000e+00 1.0000000e+00 1.2246468e-16]
[0 1 2 3]
[ 1.          2.71828183  7.3890561  20.08553692]
[0.         1.         1.41421356 1.73205081]
[[1 4 2]
 [3 2 0]]
[[1 2 4]
 [0 2 3]]
[[1 2 4]
 [0 2 3]]
[[1 2 0]
 [3 4 2]]
[(b'dipa', 2016, 8.5) (b'priya', 2015, 7. ) (b'shital', 2016, 9. )]
[(b'priya', 2015, 7. ) (b'dipa', 2016, 8.5) (b'shital', 2016, 9. )]


