
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

    def push(self, data):
        """
        Insert element to start of list
        :param data: Data to be added
        :return: Addition of data to linked list
        """

        new_node = Node(data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

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

        print("\nReverse doubly linked list:")

        while(last):
            print(str(last.data) + " "),
            last = last.prev

    def insertafter(self, loc, data):
        """
        Insert element after the given location in Doubly Linked List
        :param loc: location at which new element has to be inserted
        :return: Doubly Linked List
        """

        new_node = Node(data)
        new_node.next = loc.next
        loc.next = new_node
        new_node.prev = loc

        if new_node.next is not None:
            new_node.next.prev = new_node

    def delete_node(self, data):
        """
        Deletes the given node from Doubly Linked List
        :param: location which needs to be deleted
        :return: Doubly Linked list after deletion of node
        """

        temp = self.head

        if temp is None:
            print("Doubly Linked list is empty")

        while(temp):
            if temp.data == data:
                break
            else:
                temp = temp.next

        if temp.prev is None:
            self.head = temp.next
            temp.next.prev = None
        else:
            temp.prev.next = temp.next
            if temp.next is not None:
                temp.next.prev = temp.prev

        gc.collect()

if __name__ == "__main__":

    doubly_ll = Doubly_Linked_List()

    doubly_ll.push(3)
    doubly_ll.push(2)
    doubly_ll.push(1)

    doubly_ll.append(4)
    doubly_ll.append(5)

    doubly_ll.insertafter(doubly_ll.head.next, 15)

    print("\nDoubly Linked List after insertion:")
    doubly_ll.print_list()

    doubly_ll.delete_node(5)
    doubly_ll.delete_node(1)
    doubly_ll.delete_node(3)


    print("\n\nDoubly Linked List after deletion:")

    doubly_ll.print_list()
