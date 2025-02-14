
# This is program for Circular Linked List

# This is node structure for circular Linked List
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

# This is the class for Circular Linked List
class Circular_LL:

    def __init__(self):

        self.last = None

    def push(self, data):
        """
        Insert new node at the beginning of Circular Linked List
        :param data: Data to be inserted
        :return: Circular Linked list with insertion of new node
        """

        new_node = Node(data)
        if self.last is None:
            self.last = new_node
            self.last.next = new_node
        else:
            new_node.next = self.last.next
            self.last.next = new_node

    def append(self, data):
        """
        Insert element at the end of the list
        :param data: data to be inserted
        :return: Circular linked list
        """

        new_node = Node(data)

        new_node.next = self.last.next
        self.last.next = new_node
        self.last = new_node

    def insert_after(self, temp, data):
        """
        Insert element in between the list
        :param temp: node after which new node to be added
        :param data: data to be inserted into the new node
        :return: Circular linked list
        """

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    def delete_node(self, data):
        """
        Delete node from circular linked list
        :param data: node to be deleted
        :return: circular linked list
        """

        prev = None
        temp = self.last.next
        head = self.last.next

        while True:
            if head.data != data:
                prev = head
                head = head.next
            else:
                break

        # Check if it is single node in the list
        if head == head.next:
            self.last = None

        # If it is first node in the list
        prev = head
        while prev.next != head:
            prev = prev.next

        prev.next = head.next

        # Check if it is last node in the list
        if temp == head.next:
            prev.next = temp
            last = prev

        # Check for any other in between node
        prev.next = head.next


    '''
    def deleteSpecificNode(last, key):
    if last is None:
        # If the list is empty
        print("List is empty, nothing to delete.")
        return None

    curr = last.next
    prev = last

    # If the node to be deleted is the only node in the list
    if curr == last and curr.data == key:
        last = None
        return last

    # If the node to be deleted is the first node
    if curr.data == key:
        last.next = curr.next
        return last

    # Traverse the list to find the node to be deleted
    while curr != last and curr.data != key:
        prev = curr
        curr = curr.next

    # If the node to be deleted is found
    if curr.data == key:
        prev.next = curr.next
        if curr == last:
            last = prev
    else:
        # If the node to be deleted is not found
        print(f"Node with data {key} not found.")

    return last

    '''

    def print_list(self):
        """
        Traverse the circular Linked List
        :return: Circular Linked List
        """

        temp = self.last.next

        while (True):
            print(" " + str(temp.data) + " "),
            temp = temp.next
            if temp is self.last.next:
                break

if __name__ == "__main__":

    circular_ll = Circular_LL()

    circular_ll.push(3)
    circular_ll.push(2)
    circular_ll.push(1)

    print ("\nCircular linked list after insertion at start:")
    circular_ll.print_list()

    circular_ll.append(4)
    circular_ll.append(5)
    circular_ll.append(6)

    print ("\nCircular linked list after insertion at end:")
    circular_ll.print_list()


    circular_ll.insert_after(circular_ll.last.next, 7)
    circular_ll.insert_after(circular_ll.last.next.next, 8 )

    print ("\nCircular linked list after insertion in between the list:")
    circular_ll.print_list()

    circular_ll.delete_node(3)
    circular_ll.delete_node(1)
    circular_ll.delete_node(6)

    print ("\nCircular linked list after deletion of a node:")
    circular_ll.print_list()
