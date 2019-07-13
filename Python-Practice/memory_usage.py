



import sys 
print("Size of int in bytes", sys.getsizeof(1))
print("Empty list size in bytes", sys.getsizeof([]))
print("Empty set size in bytes", sys.getsizeof(()))
print("Empty dictionary size in bytes",sys.getsizeof({}))
print("Empty string size in bytes",sys.getsizeof(''))




Output:



Python 3.6.1 (default, Dec 2015, 13:05:11)
[GCC 4.8.2] on linux
Size of int in bytes 28
Empty list size in bytes 64
Empty set size in bytes 48
Empty dictionary size in bytes 240
Empty string size in bytes 53

