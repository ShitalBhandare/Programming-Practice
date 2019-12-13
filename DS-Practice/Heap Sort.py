

'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# Python program for implementation of heap Sort 


def heapify(arr, n, i):
    
    # Initial element = i = largest    
    largest = i
    
    # left child
    l = 2 * i + 1
    
    # Right child
    r = 2 * i + 2
    
    # Find out largest element to build max heap
    if l < n and arr[i] < arr[l]:
        largest = l
        
    if r < n and arr[largest] < arr[r]:
        largest = r
      
    # If largest is not root element, swap it 
    # and call heapify for largest element so that its subtree also get heapified
    
    if largest != i:
        
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr, n):
    
    # Build Max Heap
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    
    # Swap initial and last element 
    # Again call heapify for array (excluding last element)
    
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

if __name__ == "__main__":
    
    #arr = [3, 2, 5, 4, 1]
    arr = [12, 11, 13, 5, 6, 7]
    n = len(arr)
    heapsort(arr, n)
    print("Sorted Array:", arr)