
# This is the program to implement queue operations

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        node = Node(data)
        if self.front is None:
            self.front = node
        else:
            self.rear.next = node
        self.rear = node

    def dequeue(self):
        temp = self.front
        if temp is None:
            print ("Queue is empty")
        else:
            data_out = temp.data
            print("Data removed =>", data_out)
            temp = None
            self.front = self.front.next

            if self.front is None:
                self.rear = None

    def queueFront(self):
        if self.front is not None:
            print("Queue Front =>", self.front.data)
        else:
            print ("Queue is empty")

    def queueRear(self):
        if self.rear is not None:
            print("Queue Rear =>", self.rear.data)
        else:
            print ("Queue is empty")


    def display(self):
        temp = self.front
        while temp is not None:
            print("Data is =>",temp.data)
            temp = temp.next

if __name__ == "__main__":
    queue_obj = Queue()
    queue_obj.enqueue(1)
    queue_obj.enqueue(2)
    queue_obj.enqueue(3)
    queue_obj.enqueue(4)

    queue_obj.display()

    queue_obj.dequeue()
    queue_obj.dequeue()

    queue_obj.display()

    queue_obj.queueFront()
    queue_obj.queueRear()
