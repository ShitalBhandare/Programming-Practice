
# This program implements the Binary search
import math

def binary_search(list1, last, target):

    begin = 0
    end = last

    while(begin < end):
        mid = int(math.floor((begin + end)/2))

        if target > list1[mid]:
            begin = mid + 1
        elif target < list1[mid]:
            end = mid - 1
        else:
            begin = end + 1

    if list1[mid] == target:
        return mid
    else:
        return -1

if __name__ == "__main__":
    n = int(input("Enter the no of elements:"))
    list1 = []
    for _ in range(n):
        list1.append(int(input("Enter the element:")))

    ret = binary_search(list1, len(list1), 5)
    if ret == -1:
        print ("Target is not present in the list")
    else:
        print ("Target is present in the list at position " + str(ret))
