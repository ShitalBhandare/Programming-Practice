

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
'''
Clone a linked list with next and random pointer.

Given a linked list of size N where each node has two links: next pointer pointing to the next node and random pointer to any random node 
in the list. The task is to create a clone of this linked list.
'''


class ListNode:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.random = None
    
def cloneList(head):
    
    
    d = {}
    current = head
    while current:
        d[current] = ListNode(current.data)
        current = current.next
    
    print(d)
    current = head

    while current:
        
        newNode = d[current]
        newNode.next = d.get(current.next)
        newNode.random = d.get(current.random)
        current = current.next
        
    return d.get(head)
    
    
    
def printList(head):
    current = head
    
    while current:
        print("Next Pointer:", current.data)
        current = current.next
    
    current = head
    while current:
        if current.random:
            print("Random Pointer:", current.random.data)
            current = current.next
        
# Next:  1 -> 2 -> 3
# Random: 1 -> 3 

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next
    
    printList(head)
    clonedListHead = cloneList(head)
    print("here")
    printList(clonedListHead)
    
