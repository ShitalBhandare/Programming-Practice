# This program implements binary tree related operations.

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Binary_Tree:
    def __init__(self):
        self.root = None

    def insertnode(self, data):

        node = Node(data)
        if self.root is None:
            self.root = node
            return
        else:
            queue = []
            queue.append(self.root)
            while(True):
                chk_node = queue.pop(0)
                if chk_node.left is not None and chk_node.right is not None:
                    queue.append(chk_node.left)
                    queue.append(chk_node.right)
                else:
                    if chk_node.left is None:
                        chk_node.left = node
                        queue.append(chk_node.left)
                    elif chk_node.right is None:
                        chk_node.right = node
                        queue.append(chk_node.right)
                    break

    def preorder_traversal(self, root):

        if root is None:
            print ("Binary Tree is empty!")
            return
        else:
            print(str(root.data) + " "),
            if root.left is not None:
                self.preorder_traversal(root.left)
            if root.right is not None:
                self.preorder_traversal(root.right)

    def inorder_traversal(self, root):

        if root is None:
            print("Binary Tree is empty1")
            return
        else:
            if root.left is not None:
                #print("Here" + str(root.data))
                self.inorder_traversal(root.left)
            print(str(root.data) + " "),
            if root.right is not None:
                #print ("there" + str(root.data))
                self.inorder_traversal(root.right)

    def postorder_traversal(self, root):

        if root is None:
            print ("Binary Tree is empty!")
            return
        else:
            if root.left is not None:
                self.postorder_traversal(root.left)
            if root.right is not None:
                self.postorder_traversal(root.right)
            print (str(root.data) + " "),

    def bfirst_traversal(self, root):

        queue = []
        temp = root
        while temp is not None:
            print (str(temp.data) + " "),
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)

            if queue:
                temp = queue.pop(0)
            else:
                temp = None

    def max_depth(self, root):
        '''
        Finds height of binary tree
        :param root: root of tree
        :return: Height
        '''

        if root is None:
            return 0

        ldepth = self.max_depth(root.left)
        rdepth = self.max_depth(root.right)

        if ldepth > rdepth:
            return ldepth + 1
        else:
            return rdepth + 1

    def left_view(self, root):
        '''
        Prints left view of binary tree
        :param root:
        :return: left view
        '''

        max_level = [0]
        self.left_view_util(root, 1, max_level)

    def left_view_util(self, root, level, max_level):

        if root is None:
            return

        if  max_level[0] < level:
            print (root.data),
            max_level[0] = level

        self.left_view_util(root.left, level+1, max_level)
        self.left_view_util(root.right, level+1, max_level)

    def right_view(self, root):
        '''
        Prints right view of binary tree
        :param root:
        :return: right view
        '''

        max_level = [0]
        self.right_view_util(root, 1, max_level)

    def right_view_util(self, root, level, max_level):

        if root is None:
            return

        if max_level[0] < level:
            print(root.data),
            max_level[0] = level

        self.right_view_util(root.right, level+1, max_level)
        self.right_view_util(root.left, level+1, max_level)

    def top_view(self, root):
        '''
        Prints top view of binary tree
        :param root:
        :return:
        '''

        if root is None:
            return

        queue = []
        map = {}
        hd = 0
        root.hd = hd

        queue.append(root)

        while (len(queue)):

            root = queue[0]
            hd = root.hd

            if hd not in map:
                map[hd] = root.data

            if root.left:
                root.left.hd = hd -1
                queue.append(root.left)

            if root.right:
                root.right.hd = hd + 1
                queue.append(root.right)

            queue.pop(0)

        for i in sorted(map):
            print (map[i]),

if __name__ == "__main__":
    bin_tree = Binary_Tree()

    bin_tree.insertnode(1)
    bin_tree.insertnode(2)
    bin_tree.insertnode(3)
    bin_tree.insertnode(4)
    bin_tree.insertnode(5)

    print("\nBinary tree after Preorder traversal => ")
    bin_tree.preorder_traversal(bin_tree.root)

    print("\nBinary tree after Inorder traversal => ")
    bin_tree.inorder_traversal(bin_tree.root)

    print ("\nBinary tree after Postorder traversal => ")
    bin_tree.postorder_traversal(bin_tree.root)

    print ("\nBinary tree after Breadth First traversal => ")
    bin_tree.bfirst_traversal(bin_tree.root)

    print("\nHeight of Binary tree => "),
    print(bin_tree.max_depth(bin_tree.root))

    print("\nLeft view of binary tree => ")
    bin_tree.left_view(bin_tree.root)

    print("\nRight view of binary tree => ")
    bin_tree.right_view(bin_tree.root)

    print("\nTop view of binary tree =>")
    bin_tree.top_view(bin_tree.root)