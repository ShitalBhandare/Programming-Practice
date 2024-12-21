# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

'''
Given a binary tree, the task is to connect the nodes that are at the same level. 
Given an addition nextRight pointer for the same. 
Initially, all the next right pointers point to garbage values, set these pointers to the point next right for each node.
'''

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        self.nextRight = None
        
def connectNodesAtSameLevel(root):
    if not root:
        return
    q = []
    q.append(root)
    q.append(None)

    while q:
        node = q.pop(0)
        if node:
            node.nextRight = q[0]
            if node.left:
                q.append(node.left) 
            if node.right:
                q.append(node.right) 
        elif q:
            q. append(None) 
    return root
             
def printTree(root):
    result = []

    if not root:
        return result
        
    q = []
    q.append(root)
    q.append(None)
    
    while q:
        node = q.pop(0)
        
        if node:
            result.append(node.data)
            if node.nextRight is None:
                result.append("#")
            if node.left:
                q.append(node.left) 
            if node.right:
                q.append(node.right) 
        elif q:
            q. append(None) 
            
    return result
        
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)
    
    connectNodesAtSameLevel(root)
    result = printTree(root)
    print(" ".join(result))
    
    
