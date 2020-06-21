'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def heapify(arr, n, i):
    if i >= int(n / 2):
        return

    # Initial element = i = smallest
    smallest = i

    # left child
    l = 2 * i + 1

    # Right child
    r = 2 * i + 2

    # Find out smallest element to build min heap
    if arr[i] > arr[l]:
        smallest = l

    if r < n and arr[smallest] > arr[r]:
        smallest = r

    # If smallest is not root element, swap it
    # and call heapify for smallest element so that
    # its subtree also get heapified

    if smallest != i:
        temp = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = temp
        heapify(arr, n, smallest)

def build_heap(arr, n):
    # Build Min Heap
    i = int(n / 2) - 1
    #i = k
    while i >= 0:
        heapify(arr, n, i)
        i -= 1

def k_largest_elements(arr, n, k):
    # Build the min heap first
    build_heap(arr, n)

    i = k
    while (i < n):
        if arr[0] > arr[i]:
            continue
        else:
            arr[0] = arr[i]
            heapify(arr, n, 0)
        i += 1

if __name__ == "__main__":

    #arr = [3, 2, 5, 4, 1]
    arr = [12, 11, 5, 6, 7, 9, 25, 30]
    n = len(arr)
    k = 3
    print(arr)
    k_largest_elements(arr, n, k)
    print(arr)
    print('K largest elements are as follows:')
    for i in range(k):
        print(arr[i], end=' ')