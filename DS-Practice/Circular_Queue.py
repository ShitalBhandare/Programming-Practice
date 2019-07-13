
# This program implements Circular Queue using linked list

class Node:
    '''
    Node class to implement node functionality
    '''

    def __init__(self, data):
        self.data = data
        self.next = None

class Circular_Queue:
    '''
    This class implements the circular queue ADT and its methods
    '''

    def __init__(self):
        self.front = None
        self.rear = None

    def c_enqueue(self, data):
        '''
        Inserts element into the circular queue
        :param data: Data to be inserted
        :return: CQueue after insertion
        '''

        node = Node(data)
        if self.front is None:
            self.front = node
        else:
            self.rear.next = node
        self.rear = node
        self.rear.next = self.front

    def c_dequeue(self):
        '''
        Removes element from circular queue
        :return: Queue after deletion
        '''

        if self.front is None:
            print ("Circular queue is empty!")

        temp = self.front
        dataout = temp.data
        print("Data removed => ", dataout)
        self.front = self.front.next
        self.rear.next = self.front


    def display(self):
        '''
        Displays elements of the queue
        :return: Circular queue
        '''

        front_temp = self.front
        rear_temp = self.rear

        while (True):
            print ("Data is => ", front_temp.data)
            if front_temp is not rear_temp:
                front_temp = front_temp.next
            else:
                break


if __name__ == "__main__":

    queue_obj = Circular_Queue()
    queue_obj.c_enqueue(1)
    queue_obj.c_enqueue(2)
    queue_obj.c_enqueue(3)
    queue_obj.c_enqueue(4)

    queue_obj.display()

    queue_obj.c_dequeue()
    queue_obj.c_dequeue()

    queue_obj.display()