
# Python encapsulation

class My_class:
    
    class_var = 0
    
    def __init__(self, name, acc_no, salary):
        print("In __init__ method")
        self.name = name
        self._acc_no = acc_no
        self.__salary = salary
        
    def print(self):
        print(self.name, self._acc_no, self.__salary)
        
my_obj = My_class("Shital", 832123, 1000)
my_obj.print()
print(my_obj._acc_no)
print(My_class.class_var)
print(my_obj.class_var)
print(my_obj.__salary)



Outut =>

$python3 main.py
In __init__ method
Shital 832123 1000
832123
0
0
Traceback (most recent call last):
  File "main.py", line 22, in <module>
    print(my_obj.__salary)
AttributeError: 'My_class' object has no attribute '__salary'