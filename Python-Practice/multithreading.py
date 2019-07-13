

# Threading and synchronization

import threading
import os

def square(num):
  lock = threading.Lock()
  lock.acquire()
  print("Thread name:", threading.current_thread().name)
  print("Task ID of the process:", os.getpid())
  print(num * num)
  lock.release()

def cube(num):
  lock = threading.Lock()
  lock.acquire()
  print("Thread name:", threading.current_thread().name)
  print("Task ID of the process:", os.getpid())
  print(num*num*num)
  lock.release()

lock = threading.Lock()
t1 = threading.Thread(target=square, args=(10,), name='t1')
t2 = threading.Thread(target=cube, args=(9,), name='t2')
t1.start()
t2.start()
t1.join()
t2.join()


print("Thread finished execution")


Output:

Python 3.6.1 (default, Dec 2015, 13:05:11)
[GCC 4.8.2] on linux
Thread name: t1
Task ID of the process: 1037
100
Thread name: t2
Task ID of the process: 1037
729
Thread finished execution
