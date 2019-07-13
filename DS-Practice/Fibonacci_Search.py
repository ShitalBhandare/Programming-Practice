

# This program implements the Fibonacci Search

def fibonacci_search(list1, last, target):

    fibm2 = 0
    fibm1 = 1
    fibm = fibm1 + fibm2

    offset = -1

    while (fibm < last):
        fibm2 = fibm1
        fibm1 = fibm
        fibm = fibm1 + fibm2

    i = min(offset+fibm2, last-1)
    while(fibm > 1):

        if list1[i] > target:
            fibm = fibm2
            fibm1 = fibm1 - fibm
            fibm2 = fibm1 - fibm2


        elif(list1[i] < target):

            fibm = fibm1
            fibm1 = fibm2
            fibm2 = fibm - fibm1
            offset = i

        else:
            return i

    if (fibm1 and list1[offset + 1] == target):
        return offset + 1

    return -1


if __name__ == "__main__":
    n = int(input("Enter the no of elements:"))
    list1 = []
    for _ in range(n):
        list1.append(int(input("Enter the element:")))

    ret = fibonacci_search(list1, len(list1),5)
    if ret == -1:
        print ("Target is not present in the list")
    else:
        print ("Target is present in the list at position " + str(ret))



