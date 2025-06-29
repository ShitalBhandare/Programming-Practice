# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it

'''
Problem: Check if height is balanced
'''


class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

def isBalanced(root):
    if not root:
        return True
    
    lheight = getHeight(root.left)
    rheight = getHeight(root.right)
    
    if abs(lheight - rheight) > 1:
        return False
        
    return isBalanced(root.left) and isBalanced(root.right)
    
    
def getHeight(node):
    if not node:
        return 0
        
    lheight = getHeight(node.left)
    rheight = getHeight(node.right)
    
    return max(lheight, rheight) + 1
    
if __name__ == "__main__":
    # Representation of input BST:
    #            1
    #           / \
    #          2   3
    #         /  \
    #        4   5 
    #       /
    #      8
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    #root.right.right = Node(9)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(8)

    print("True" if isBalanced(root) else "False")   
