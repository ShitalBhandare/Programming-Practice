
# This program is for linear search

def linear_search(list1, target):
    for i in range(len(list1)):
        if list1[i] == target:
            return i
    return -1

if __name__ == "__main__":
    n = int(input("Enter the no of elements:"))
    list1 = []
    for _ in range(n):
        list1.append(int(input("Enter the element:")))

    ret = linear_search(list1, 5)
    if ret == -1:
        print ("Target is not present in the list")
    else:
        print ("Target is present in the list at position " + str(ret))








