
# Program to implement reverse list in size of k
# Input => 1 2 3 4 5 6 and k =3
# output => 3 2 1 6 5 4



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

    # Reverse a singly linked list
    def reverse_list(self, head, k):
        current = head
        prev = None
        next = None
        count = 0

        while (current and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
        
        if next: 
            head.next = self.reverse_list(next, k)

        return prev


    # Print all the elements in the list
    def print_llist(self):

        temp = self.head
        while(temp):
            print(str(temp.data) + " "),
            temp = temp.next


if __name__ == '__main__':
    singly_ll = Linked_List()

    singly_ll.push(0)

    # Append element to the list
    singly_ll.append(1)
    singly_ll.append(2)
    singly_ll.append(3)
    singly_ll.append(4)
    singly_ll.append(5)
    singly_ll.append(6)

    # Print element of a list
    singly_ll.print_llist()
    
    # Reverse list in size of k
    sys.stdout.write("\n\nLinked list after reversal\n")
    singly_ll.head = singly_ll.reverse_list(singly_ll.head, 3)
    
    # Print element of a list
    singly_ll.print_llist()
    




