
import inspect, sys
arr = []
prev = -2187543620

# Structure of a Binary Tree Node
class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

def isBST(root):
    flag = 0
    inOrder(root)
    print(arr)
    arr1 = arr
    arr1.sort()
    print(arr1)

    if (arr == arr1):
        flag = 1

    if flag:
        print("true")
    else:
        print("false")

def inOrder(root):

    if root == None:
        return
    inOrder(root.left)


    print(root.data)
    curr = root.data
    # if curr < prev:
    #    return false
    arr.append(root.data)

    # Below code checks how recursion works
    current_frame = inspect.currentframe()
    calframe = inspect.getouterframes(current_frame, 2)

    frame_object = calframe[0][0]
    #print("Recursion-%d: %s" % (max_recursion_depth - recursion_index, frame_object.f_locals))
    print("Passed parameters: %s" % (sys._getframe(1).f_locals))

    inOrder(root.right)


if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.right = Node(6)

    # Function call
    print("Inorder traversal of binary tree is: ")
    isBST(root)


'''
Input:

           4
         /   \
        2     5
      /  \     \
     1    3     6

Output:

/usr/bin/python3 /Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py 
Inorder traversal of binary tree is: 
1
Passed parameters: {'root': <__main__.Node object at 0x108877f70>}
2
Passed parameters: {'root': <__main__.Node object at 0x108877fd0>}
3
Passed parameters: {'root': <__main__.Node object at 0x108877f70>, 'current_frame': <frame at 0x108a25780, file '/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', line 45, code inOrder>, 'calframe': [FrameInfo(frame=<frame at 0x108a25780, file '/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', line 45, code inOrder>, filename='/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', lineno=39, function='inOrder', code_context=['    current_frame = inspect.currentframe()\n', '    calframe = inspect.getouterframes(current_frame, 2)\n'], index=1), FrameInfo(frame=<frame at 0x108a255b0, file '/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', line 32, code inOrder>, filename='/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', lineno=32, function='inOrder', code_context=['        return\n', '    inOrder(root.left)\n'], index=1), FrameInfo(frame=<frame at 0x10881f800, file '/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', line 14, code isBST>, filename='/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', lineno=14, function='isBST', code_context=['    flag = 0\n', '    inOrder(root)\n'], index=1), FrameInfo(frame=<frame at 0x7fcf427249d0, file '/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', line 58, code <module>>, filename='/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', lineno=58, function='<module>', code_context=['    print("Inorder traversal of binary tree is: ")\n', '    isBST(root)\n'], index=1)], 'frame_object': <frame at 0x108a25780, file '/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', line 45, code inOrder>}
4
Passed parameters: {'root': <__main__.Node object at 0x108877fd0>, 'flag': 0}
5
Passed parameters: {'root': <__main__.Node object at 0x108877fd0>, 'current_frame': <frame at 0x108a255b0, file '/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', line 45, code inOrder>, 'calframe': [FrameInfo(frame=<frame at 0x108a255b0, file '/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', line 45, code inOrder>, filename='/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', lineno=39, function='inOrder', code_context=['    current_frame = inspect.currentframe()\n', '    calframe = inspect.getouterframes(current_frame, 2)\n'], index=1), FrameInfo(frame=<frame at 0x10881f800, file '/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', line 14, code isBST>, filename='/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', lineno=14, function='isBST', code_context=['    flag = 0\n', '    inOrder(root)\n'], index=1), FrameInfo(frame=<frame at 0x7fcf427249d0, file '/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', line 58, code <module>>, filename='/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', lineno=58, function='<module>', code_context=['    print("Inorder traversal of binary tree is: ")\n', '    isBST(root)\n'], index=1)], 'frame_object': <frame at 0x108a255b0, file '/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', line 45, code inOrder>}
6
Passed parameters: {'root': <__main__.Node object at 0x108877f10>, 'current_frame': <frame at 0x7fcf43205130, file '/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', line 45, code inOrder>, 'calframe': [FrameInfo(frame=<frame at 0x7fcf43205130, file '/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', line 45, code inOrder>, filename='/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', lineno=39, function='inOrder', code_context=['    current_frame = inspect.currentframe()\n', '    calframe = inspect.getouterframes(current_frame, 2)\n'], index=1), FrameInfo(frame=<frame at 0x108a255b0, file '/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', line 45, code inOrder>, filename='/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', lineno=45, function='inOrder', code_context=['\n', '    inOrder(root.right)\n'], index=1), FrameInfo(frame=<frame at 0x10881f800, file '/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', line 14, code isBST>, filename='/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', lineno=14, function='isBST', code_context=['    flag = 0\n', '    inOrder(root)\n'], index=1), FrameInfo(frame=<frame at 0x7fcf427249d0, file '/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', line 58, code <module>>, filename='/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', lineno=58, function='<module>', code_context=['    print("Inorder traversal of binary tree is: ")\n', '    isBST(root)\n'], index=1)], 'frame_object': <frame at 0x7fcf43205130, file '/Users/shital.bhandare/inSync Work/Git Repos/SHSrv/src/shsrv/bl/compaction_processor/isBST.py', line 45, code inOrder>}
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
true
  

'''


'''
Program for not using array:

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def isBST(node, prev):
    if node is None:
        return True
    
    if not isBST(node.left, prev):
        return False
    if prev[0] is not None and prev[0] > node.data:
       return False
    
    prev[0] = node.data

    print(node.data, prev)
    return isBST(node.right, prev) 

if __name__ == "__main__":
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    root.left.left = Node(6)
    prev = [None]
    print(isBST(root, prev))
   

prev[0] = None, 1, 2 
   
'''
  2                       
/   \
1    3
  
Result:   

[1, 2, 3]    
prev = 3
    
'''


'''






