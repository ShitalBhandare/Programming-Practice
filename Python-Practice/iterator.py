
# More convenient way
list1 = [1, 2, 3, 4]
for item in list1:
    print(item)
    
print("Using iter and next methods:")
# Using Iterator methods
list2 = [5, 6, 7, 8]

iter_obj = iter(list2)

print(next(iter_obj))

print(next(iter_obj))

print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
    
	
OUTPUT:

1
2
3
4
Using iter and next methods:
5
6
7
8
Traceback (most recent call last):
  File "main.py", line 19, in <module>
    print(next(iter_obj))
StopIteration