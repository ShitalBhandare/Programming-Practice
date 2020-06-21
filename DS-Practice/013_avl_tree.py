# This is the program for AVL Tree (Self Balancing Binary Search Tree)

class Node:
    '''
    Class to create Node in AVL tree
    '''

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree:
    '''
    This is the class for AVL Tree
    '''

    def insert_node(self, root, data):
        '''
        Inserts node in AVL tree
        :param val: val to be inserted
        :return: AVL Tree after insertion
        '''

        if not root:
            return Node(data)
        elif data < root.data:
            root.left = self.insert_node(root.left, data)
        else:
            root.right = self.insert_node(root.right, data)


        # Calculate Height
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Calculate Balance Factor
        balance = self.getBalance(root)

        # Right Right Case:
        if balance < -1 and data > root.right.data:
            return self.left_rotate(root)

        # Left Left Case:
        if balance > 1 and data < root.left.data:
            return self.right_rotate(root)


        # Left Right Case:
        if balance > 1 and data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case:
        if balance < -1 and data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root


    def delete_node(self, root, key):
        '''
        Deletes the node from AVL tree
        :param root: root of tree
        :return: tree after deletion
        '''

        if root is None:
            return

        # Perform delete node like BST
        if key < root.data:
            root.left = self.delete_node(root.left, key)
        elif key > root.data:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            else:
                largest = self.findLargest(root.left)
                root.data = largest.data
                root.left = self.delete_node(root.left, largest.data)

        if root is None:
            return root

        # Get the height of ancestor node
        height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Get the balance factor
        balance = self.getBalance(root)

        # If node is unbalanced try out 4 cases

        # Left Left Case:
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.right_rotate(root)

        # Right Right Case:
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.left_rotate(root)

        # Right-Left Case:
        if balance < -1  and self.getBalance(root.right) > 0:
            self.right_rotate(root.left)
            return self.left_rotate(root)

        # Left-Right Case:
        if balance > 1 and self.getBalance(root.left) < 0:
            self.left_rotate(root.right)
            return self.right_rotate(root)

        return root

    def findLargest(self, root):
        '''
        Finds the largest node in the tree
        :param root: root of tree
        :return: largest node data in the tree
        '''

        current = root

        while current.right is not None:
            current = current.right
        else:
            return current
        
        '''
   z                                y
 /  \                            /   \ 
T1   y     Left Rotate(z)       z      x
    /  \   - - - - - - - ->    / \    / \
   T2   x                     T1  T2 T3  T4
       / \
     T3  T4
  
        '''
        
    def left_rotate(self, z):
        '''
        Performs left rotation of tree
        :param z: root
        :return: left rotated tree
        '''

        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        # Update Heights
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))

        return y

    '''
    
    T1, T2, T3 and T4 are subtrees.
         z                                      y 
        / \                                   /   \
       y   T4      Right Rotate (z)          x      z
      / \          - - - - - - - - ->      /  \    /  \ 
     x   T3                               T1  T2  T3  T4
    / \
  T1   T2
  
    '''
    
    def right_rotate(self, z):
        '''
        Performs Right rotation
        :param root: root
        :return: right rotated tree
        '''

        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        # Update Heights
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))

        return y

    def getHeight(self, root):
        '''
        Calculates the height of tree
        :param root: root
        :return: height
        '''

        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        '''
        Gets balance factor of the tree
        :param root: root
        :return: balance factor
        '''

        if not root:
            return 0

        return (self.getHeight(root.left) - self.getHeight(root.right))

    def preOrder(self, root):
        '''
        Preorder Traversal of tree
        :param root: root of tree
        :return: preorder traversal
        '''

        if not root:
            return
        print(root.data),
        self.preOrder(root.left)
        self.preOrder(root.right)


if __name__ == "__main__":
    avl_obj = AVL_Tree()

    root = None

    # Inserts node in the tree
    root = avl_obj.insert_node(root, 10)
    root = avl_obj.insert_node(root, 20)
    root = avl_obj.insert_node(root, 30)
    root = avl_obj.insert_node(root, 40)
    root = avl_obj.insert_node(root, 50)
    root = avl_obj.insert_node(root, 25)

    # Preorder Traversal of tree
    print('\nAVL Tree elements after insertion:')
    avl_obj.preOrder(root)

    # Deletes node from the tree
    root = avl_obj.delete_node(root, 50)

    # Preorder Traversal of tree
    print('\nAVL Tree elements after deletion of element 50:')
    avl_obj.preOrder(root)
