# This program is for sentinel search


# This program is for linear search

def sentinel_search(list1, target):
    list1.append(target)
    i = 0
    while(list1[i] != target):
        i += 1
    return i

if __name__ == "__main__":
    n = int(input("Enter the no of elements:"))
    list1 = []
    for _ in range(n):
        list1.append(int(input("Enter the element:")))

    length = len(list1)
    ret = sentinel_search(list1, 5)
    if ret > length - 1:
        print ("Target is not present in the list")
    else:
        print ("Target is present in the list at position " + str(ret))








