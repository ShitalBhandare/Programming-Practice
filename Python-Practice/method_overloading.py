# Method Overloading in Python

# Python does not support method overloading
# Still, we can achieve it using following ways:

# 1. from pythonlangutil.overload import Overload, signature
# Using overload decorator


# 2. Using single method:

def calc(size=None, length=None, breadth=None):
    if size is not None:
        return size * size
        
    if length is not None and breadth is not None:
        return length * breadth
        

print(calc(3))
print(calc(length = 4, breadth = 5))

# 3. Using below format

def add(datatype, * args):
    if datatype == "int":
        answer = 0
    if datatype == "str":
        answer = ""
        
    for x in args:
        answer = answer + x
        
    print(answer)

add("int", 5, 6)
add("str", "Hi", " Shital")


Output ==>
$python3 main.py
9
20
11
Hi Shital