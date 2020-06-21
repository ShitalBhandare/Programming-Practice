
import os
import math
import sys

# Class to implement Node structure i.e. Data and pointer field
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Class to implement singly linked list
class Linked_List:

    # Class constructor
    def __init__(self):
        self.head = None

    # Insert element at the start of list
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Append element to end of the list
    def append(self, data):
        temp = self.head
        while (temp.next):
            temp = temp.next

        new_node = Node(data)
        temp.next = new_node

    # Insert element in the middle of a list
    def insert(self, data, loc):
        temp = self.head

        while (temp.data):
            if temp.data == loc:
                break
            else:
                temp = temp.next

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    # Delete given node from linked list
    def delete_node(self, loc):

        temp = self.head

        if temp.data == loc:
            self.head = temp.next
            temp = None
            return

        while (temp.data):
            if temp.data == loc:
                break

            prev = temp
            temp = temp.next

        prev.next = temp.next
        temp = None
        return

    # Reverse a singly linked list
    def reverse_list(self):
        current = self.head
        prev = None

        while (current):
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev


    # Print all the elements in the list
    def print_llist(self):

        temp = self.head
        while(temp):
            print(str(temp.data) + " "),
            temp = temp.next


if __name__ == '__main__':
    singly_ll = Linked_List()

    sys.stdout.write("Start => ")

    # Insert element at the start of the list
    singly_ll.push(1)
    singly_ll.push(2)
    singly_ll.push(3)

    # Append element to the list
    singly_ll.append(4)
    singly_ll.append(5)
    singly_ll.append(6)

    # Insert element in the middle of the list
    singly_ll.insert(7, 4)
    singly_ll.insert(8, 5)
    singly_ll.insert(9, 6)

    # Print element of a list
    singly_ll.print_llist()

    sys.stdout.write("End")

    # Delete element from the list
    sys.stdout.write("\n\nLinked list after deletion of 4\n")
    singly_ll.delete_node(4)
    singly_ll.print_llist()

    sys.stdout.write("\n\nLinked list after deletion of 3\n")
    singly_ll.delete_node(3)
    singly_ll.print_llist()

    sys.stdout.write("\n\nLinked list after deletion of 9\n")
    singly_ll.delete_node(9)
    singly_ll.print_llist()


    # Reverse a singly linked list
    sys.stdout.write("\n\nLinked list after reversal\n")
    singly_ll.reverse_list()
    singly_ll.print_llist()