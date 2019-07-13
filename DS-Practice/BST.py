# This program implements binary tree related operations.

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Binary_Tree:
    def __init__(self):
        self.root = None

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


    def findSmallestBST(self, root):
        """
        Returns smallest node data from BST
        :param root: root
        :return: smallest node
        """

        if root.left is None:
            print(root.data)
        else:
            self.findSmallestBST(root.left)

    def findLargestBST(self, root):
        """
        Returns largest node from BST
        :param root: root node
        :return: largest node
        """

        current = root

        while current.right is not None:
            current = current.right
        else:
            return current

    def searchBST(self, root, data):
        """
        Search requested node in BST
        :param data: node to be searched
        :return: True on success else False
        """

        if root.data == data:
            print("Search Successful")
            return
        if root.data > data:
            self.searchBST(root.left, data)
        else:
            self.searchBST(root.right, data)

    def insertnodeBST(self, root, data):
        """
        Inserts node into BST
        :param root: root node
        :param data: data to be inserted
        :return: tree after insertion
        """

        if self.root is None:
            self.root = Node(data)
        elif root is None:
            root = Node(data)
        else:
            if data < root.data:
                if root.left:
                    self.insertnodeBST(root.left, data)
                else:
                    root.left = Node(data)
            else:
                if root.right:
                    self.insertnodeBST(root.right, data)
                else:
                    root.right = Node(data)
        return

    def deleteNodeBST(self, root, data):
        """
        Deletes the node from BST
        :param root: Root node of the tree
        :param data: node to be deleted
        :return: BST after deletion
        """




        if root is None:
            return root

        if data > root.data:
            root.right = self.deleteNodeBST(root.right, data)
        elif data < root.data:
            root.left = self.deleteNodeBST(root.left, data)
        else:
            if root.left is None:
                # Make right node as parent node

                temp = root.right
                root = None
                return temp

            elif root.right is None:
                # Make Left node as parent node

                temp = root.left
                root = None
                return temp

            largest = self.findLargestBST(root.left)
            if largest:
                root.data = largest.data
                root.left = self.deleteNodeBST(root.left, largest.data)

        return root

if __name__ == "__main__":
    bin_tree = Binary_Tree()

    bin_tree.insertnodeBST(bin_tree.root, 10)
    bin_tree.insertnodeBST(bin_tree.root, 15)
    bin_tree.insertnodeBST(bin_tree.root, 5)
    bin_tree.insertnodeBST(bin_tree.root, 3)
    bin_tree.insertnodeBST(bin_tree.root, 7)

    print("\nBinary tree after Inorder traversal => ")
    bin_tree.inorder_traversal(bin_tree.root)

    #print("\nSmallest node in the binary search tree => ")
    #bin_tree.findSmallestBST(bin_tree.root)

    #print("\nLargest node in the binary search tree => ")
    #bin_tree.findLargestBST(bin_tree.root)

    #print("\nRequested node search in the binary search tree => ")
    #bin_tree.searchBST(bin_tree.root, 10)

    print ("\nDeleting the node from BST")
    root = bin_tree.deleteNodeBST(bin_tree.root, 15)

    print("\nBinary tree after Inorder traversal => ")
    bin_tree.inorder_traversal(bin_tree.root)


