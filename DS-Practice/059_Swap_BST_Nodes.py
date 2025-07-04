# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
'''
Problem:

Given a Binary Search Tree (BST) with Two nodes swapped, the task is to recover the original BST. 
I/P:
            1
           / \
           3 2
           
O/P:
            1
           / \
           2  3
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def correctBSTUtil(root, prev, first, middle, last):
    if root is None:
        return
        
    correctBSTUtil(root.left, prev, first, middle, last)
    
    if prev[0] and root.data < prev[0].data:
        if not first[0]:
            first[0] = prev[0]
            middle[0] = root
        else:
            last[0] = root
            
    prev[0] = root
    
    correctBSTUtil(root.right, prev, first, middle, last)

def correctBST(root):
    
    prev, first, middle, last = [None],  [None],  [None],  [None]
    correctBSTUtil(root, prev, first, middle, last)
    
    if first[0] and last[0]:
        first[0].data, last[0].data = last[0].data, first[0].data
    elif first[0] and middle[0]:
        first[0].data, middle[0].data = middle[0].data, first[0].data
# Print tree as level order

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)
    
    
def printLevelOrder(root):
    if not root:
        print("N", end=" ")
        return

    queue = [root]
    nonNull = 1

    while queue and nonNull > 0:
        curr = queue.pop(0)

        if curr is None:
            print("N", end=" ")
            continue
        nonNull -= 1

        print(curr.data, end=" ")
        queue.append(curr.left)
        queue.append(curr.right)
        if curr.left:
            nonNull += 1
        if curr.right:
            nonNull += 1

if __name__ == "__main__":
    # Constructing the tree with swapped nodes
    #       6
    #     /  \
    #    10   2
    #   / \  / \
    #  1  3 7  12
    # Here, 10 and 2 are swapped

    root = Node(6)
    root.left = Node(10)
    root.right = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.right = Node(12)
    root.right.left = Node(7)

    print("Before swapping:")
    #printLevelOrder(root)
    inorder(root)
    correctBST(root)
    print("\nAfter swapping:")
    #printLevelOrder(root)
    inorder(root)
    
