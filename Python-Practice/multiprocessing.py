


# Multiprocessing in python

import multiprocessing
import os

def square(num):
  
  print("\nProcess name:", multiprocessing.current_process().name)
  print("Process ID of the process:", os.getpid())
  print(num * num)
  

def cube(num):
  
  print("\nProcess name:", multiprocessing.current_process().name)
  print("Process ID of the process:", os.getpid())
  print(num*num*num)
  

print("Process ID of the process:", os.getpid())
p1 = multiprocessing.Process(target=square, args=(10,), name='p1')
p2 = multiprocessing.Process(target=cube, args=(9,),name='p2')


p1.start()
p2.start()

p1.join()
p2.join()


print("Thread finished execution")


Output:

Python 3.6.1 (default, Dec 2015, 13:05:11)
[GCC 4.8.2] on linux
Process ID of the process: 1363

Process name: p1
Process ID of the process: 1368
100

Process name: p2
Process ID of the process: 1369
729
Thread finished execution