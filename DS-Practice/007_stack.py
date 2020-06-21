#
# This program will implement the basic operations on Stack like push, pop, top, display
# using singly linked list
#

class Node:
    '''
    Node class to create node in linked list
    '''

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    '''
    Stack class to perform stack operations
    '''

    def __init__(self):
        self.top = None

    def push(self, data):
        '''
        Inserts element into the stack
        :param data: data to be inserted
        :return: stack after insertion
        '''

        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        '''
        Removes element from the stack
        :return: stack after deletion
        '''

        if self.top is not None:
            pop_data = self.top.data
            self.top = self.top.next
        else:
            print ("Stack is empty")

    def peek(self):
        '''
        Return element at top of the stack
        :return: Top element
        '''
        if self.top is not None:
            return self.top.data
        else:
            print ("Stack is empty")

    def display(self):
        '''
        Displays element of stack one by one
        :return: Entire stack list
        '''

        temp = self.top
        while temp is not None:
            print("Node Data =>", temp.data)
            temp = temp.next

if __name__ == "__main__":
    st_obj = Stack()
    print("Elements of stack after push")
    st_obj.push(1)
    st_obj.push(2)
    st_obj.push(3)
    st_obj.push(8)
    st_obj.display()

    print("Elements of stack after pop")
    st_obj.pop()
    st_obj.pop()
    #st_obj.pop()
    #st_obj.pop()
    st_obj.display()

    print("Element of stack at the top")
    top_data = st_obj.peek()
    print (top_data)
    st_obj.display()
