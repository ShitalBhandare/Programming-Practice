# This code is for Doubly Linked List

import gc

# Node class
class Node:

    def __init__(self, data):

        self.data = data
        self.prev = None
        self.next = None

# Doubly Linked List class
class Doubly_Linked_List:

    def __init__(self):

        self.head = None

    def append(self, data):
        """
        Append an element to doubly linked list
        :param data: Data to be appended
        :return: Doubly LL
        """

        new_node = Node(data)

        temp = self.head
        last = None

        if temp is None:
            self.head = new_node
            return

        while(temp):
            last = temp
            temp = temp.next

        last.next = new_node
        new_node.prev = last


    def print_list(self):
        """
        Print all elements in the list
        :return: Doubly LL
        """

        tmp = self.head
        while(tmp):
            print(str(tmp.data) + " "),
            last = tmp
            tmp = tmp.next

    def reverse_list(self, head):
        """
        Reverses doubly linked list using pointers
        """

        current = head
        
        while(current):
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
            
        if temp:
            self.head = temp.prev
            

if __name__ == "__main__":

    doubly_ll = Doubly_Linked_List()
    
    print("\nDoubly Linked List after insertion:")
    doubly_ll.append(1)
    doubly_ll.append(2)
    doubly_ll.append(3)
    doubly_ll.append(4)
    doubly_ll.print_list()

    print("\n\nDoubly linked list after reversal:")
    doubly_ll.reverse_list(doubly_ll.head)
    doubly_ll.print_list()