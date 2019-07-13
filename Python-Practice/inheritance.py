# Inheritance in Python

# 1. Single Inheritance

print("Single Inheritance Output:")

class Father:
    def print_name(self, name):
        print("In Father class")
        print("Name: ", name)
        
class Child(Father):
    def print_age(self, age):
        print("In Child class")
        print("Age: ", age)
        
c_obj = Child()
c_obj.print_name("Shital")
c_obj.print_age(23)

# 2. Multilevel Inheritance

print("\n\nMultilevel Inheritance Output:")

class Grandfather(object):
    def speak(self):
        print("In Grandfather class")

class Father(Grandfather):
    def print_name(self, name):
        print("In Father class")
        print("Name: ", name)
        
class Child(Father):
    def print_age(self, age):
        print("In Child class")
        print("Age: ", age)
        
c_obj = Child()
c_obj.speak()
c_obj.print_name("Priya")
c_obj.print_age(2)


# 3. Multiple Inheritance

print("\n\nMultiple Inheritance Output:")

class Mother(object):
    def speak(self):
        print("In Mother class")

class Father(object):
    def print_name(self, name):
        print("In Father class")
        print("Name: ", name)
        
class Child(Father, Mother):
    def print_age(self, age):
        print("In Child class")
        print("Age: ", age)
        
c_obj = Child()
c_obj.speak()
c_obj.print_name("Geeta")
c_obj.print_age(21)


# 4. Hierarchical Inheritance

print("\n\nHierarchical Inheritance Output:")

class Father(object):
    def print_name(self, name):
        print("In Father class")
        print("Name: ", name)
        
class Child1(Father):
    def print_age(self, age):
        print("In Child1 class")
        print("Age: ", age)
        
class Child2(Father):
    def print_dob(self, dob):
        print("In Child2 class")
        print("DoB: ", dob)
        
c_obj = Child1()
c_obj.print_name("Geeta")
c_obj.print_age(21)
c2_obj = Child2()
c2_obj.print_dob("1/1/2018")


# 5. Hybrid Inheritance

print("\n\nHybrid Inheritance Output:")

class Grandfather(object):
    def speak(self):
        print("In Grandfather class")
        
class Father(Grandfather):
    def print_name(self, name):
        print("In Father class")
        print("Name: ", name)
        
class Child1(Father):
    def print_age(self, age):
        print("In Child1 class")
        print("Age: ", age)
        
class Child2(Father):
    def print_dob(self, dob):
        print("In Child2 class")
        print("DoB: ", dob)
        
c_obj = Child1()
c_obj.print_name("Geeta")
c_obj.print_age(21)
c_obj.speak()
c2_obj = Child2()
c2_obj.print_dob("1/1/2018")

# 6. Data abstraction / Private members of the class

print("\n\n\nData abstraction / Private members of the class output: ")
class Father:
    def print_name(self, name):
        __priv_var = 1
        print("In Father class")
        print("Name: ", name)
        
class Child(Father):
    def print_age(self, age):
        print("In Child class")
        print("Age: ", age)
        
c_obj = Child()
c_obj.print_name("Shital")
c_obj.print_age(23)
print(c_obj.__priv_var)




Output: ==> 
$python3 main.py
Single Inheritance Output:
In Father class
Name:  Shital
In Child class
Age:  23


Multilevel Inheritance Output:
In Grandfather class
In Father class
Name:  Priya
In Child class
Age:  2


Multiple Inheritance Output:
In Mother class
In Father class
Name:  Geeta
In Child class
Age:  21


Hierarchical Inheritance Output:
In Father class
Name:  Geeta
In Child1 class
Age:  21
In Child2 class
DoB:  1/1/2018


Hybrid Inheritance Output:
In Father class
Name:  Geeta
In Child1 class
Age:  21
In Grandfather class
In Child2 class
DoB:  1/1/2018



Data abstraction / Private members of the class output: 
In Father class
Name:  Shital
In Child class
Age:  23
Traceback (most recent call last):
  File "main.py", line 142, in <module>
    print(c_obj.__priv_var)
AttributeError: 'Child' object has no attribute '__priv_var'
























