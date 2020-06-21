

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
                
    def get_max_width(self, root):
        
        if root is None:
            return 0
        
        queue = []
        queue.append(root)
        
        max_width = 0
        
        while(queue):
            
            count = len(queue)
            max_width = max(count, max_width)
            
            while(count):
                
                count -= 1
                temp = queue.pop(0)
                
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)

        return  max_width 
    
if __name__ == "__main__":
    
    btree = Binary_Tree()
    btree.addnode(10)
    #btree.addnode(20)
    btree.addnode(30)
    btree.addnode(40)
    #btree.addnode(50)
    btree.addnode(60)
    btree.addnode(70)
    btree.addnode(70)
    
    print("\nPre-Order Traversal of Tree is as follows:\n")
    btree.preorder(btree.root)
    
    width = btree.get_max_width(btree.root)
    print("\n\nThe maximum width of binary tree is", width)
    
