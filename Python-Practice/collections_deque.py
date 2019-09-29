
#Implementation of stack and queue using collections.deque
    
from collections import deque

list1 = [1, 2, 3, 4, 5]
d = deque(list1)
print(d)
d.append(6)
print(d)
print(d.pop())

d.appendleft(0)
print(d)
print(d.popleft())
print(d)

print("here")
print(list(d))


Output ==> 

$python3 main.py
deque([1, 2, 3, 4, 5])
deque([1, 2, 3, 4, 5, 6])
6
deque([0, 1, 2, 3, 4, 5])
0
deque([1, 2, 3, 4, 5])
here
[1, 2, 3, 4, 5]
