'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# Program to print top view of Binary Tree:

# This program does not use horizontal distance in tree data structure
# It uses modified Pre-Order traversal like logic

class Node:
    
    def __init__(self, data):
        
        self.left = None
        self.right = None
        self.data = data
        
class Binary_Tree:
    
    def __init__(self):
        self.root = None
        
    def addnode(self, data):
        node = Node(data)
        
        if not self.root:
            self.root = node
        
        else:
            queue = []
            queue.append(self.root)
            while queue:
                root = queue.pop(0)
                if root.left:
                    queue.append(root.left)
                else:
                    root.left = node
                    break
                if root.right:
                    queue.append(root.right)
                else:
                    root.right = node
                    break
                
        
    def preorder(self, root):
        
        if root is None:
            return
        
        print(root.data, end=" ")
        
        if root.left:
            self.preorder(root.left)
        if root.right:
            self.preorder(root.right)
        
        
    def print_top_view(self, root):
        
        top_view = {}
        queue = []
        hd = 0
        queue.append([root, hd])
        
        while queue:
            
            item = queue.pop(0)
            temp = item[0]
            hd = item[1]
            
            if hd not in top_view:
                top_view[hd] = temp.data
        
            if temp.left:
                queue.append([temp.left, hd-1])
            
            if temp.right: 
                queue.append([temp.right, hd+1])
        
        for item in sorted(top_view):
            print(top_view[item], end = " ")
            
if __name__ == "__main__":
    
    btree = Binary_Tree()
    btree.addnode(10)
    btree.addnode(20)
    btree.addnode(30)
    btree.addnode(40)
    btree.addnode(50)
    btree.addnode(60)
    btree.addnode(70)
    

    print("\nPre-Order Traversal of Tree is as follows:\n")
    btree.preorder(btree.root)
    
    print("\nTop View of Tree is as follows:\n")
    btree.print_top_view(btree.root)