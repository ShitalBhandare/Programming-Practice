
# Method Overriding in Python

class A:
    def new_method(self):
        print("In method A")
    
class B(A):
    def new_method(self):
        print("In method B")
		
        
b = B()
b.new_method()


output ==>

$python3 main.py
In method B
