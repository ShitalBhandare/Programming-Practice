

# Program to print maximum level sum of binary tree

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
        
    def get_max_level_sum(self, root):
        
        if root is None:
            return 0
        
        max_sum = root.data
        queue = []
        queue.append(root)
        
        while(queue):
            
            count = len(queue)
            sum = 0
            
            while(count):
                
                count -= 1
                temp = queue.pop(0)
                sum = sum + temp.data
                
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                    
            max_sum = max(sum, max_sum)

        return  max_sum 
    
if __name__ == "__main__":
    
    btree = Binary_Tree()
    btree.addnode(1)
    btree.addnode(2)
    btree.addnode(3)
    btree.addnode(4)
    btree.addnode(5)
    btree.addnode(-8)
    
    print("\nPre-Order Traversal of Tree is as follows:\n")
    btree.preorder(btree.root)
    
    max_sum = btree.get_max_level_sum(btree.root)
    print("\n\nThe maximum width of binary tree is", max_sum)
    
