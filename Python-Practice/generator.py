# Use of Generator in python

class fib:
    def fib_series(self, num):
        a, b = 0, 1
        while num > 0:
            a, b = b, a + b
            yield b
            num = num - 1
        
        
f_obj = fib()
val = f_obj.fib_series(5)
print("Fibbonanci series:", val)

print(val.next())
print(val.next())
print(val.next())
print(val.next())
print(val.next())


# Generator Expressions:

result = (i**2 for i in range(3))
print(result)
print(result.next())
print(result.next())
print(result.next())
print(result.next())


Output:
('Fibbonanci series:', <generator object fib_series at 0x7f11e94cd550>)
1
2
3
5
8
<generator object <genexpr> at 0x7f11e94cd5a0>
0
1
4
Traceback (most recent call last):
  File "main.py", line 30, in <module>
    print(result.next())
StopIteration

    
