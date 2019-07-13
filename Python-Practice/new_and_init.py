
# New a nd init magic methods in python


class new_class():
    def __new__(cls):
        print("In new method")
        instance = object.__new__(cls)
        return instance
        
        
    def __init__(self):
        print("In init method")
        return 5
        
a = new_class()
print(a)



Output:

In new method
In init method
Traceback (most recent call last):
  File "main.py", line 16, in <module>
    a = new_class()
TypeError: __init__() should return None, not 'int'