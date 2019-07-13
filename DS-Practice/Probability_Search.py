
# This program is for linear search

def probability_search(list1, target):
    for i in range(len(list1)):
        if list1[i] == target:
            if i >= 1:
                temp = list1[i-1]
                list1[i-1]= list1[i]
                list1[i]=temp
            return True
    return False

if __name__ == "__main__":
    n = int(input("Enter the no of elements:"))
    list1 = []
    for _ in range(n):
        list1.append(int(input("Enter the element:")))

    ret = probability_search(list1, 5)
    if ret:
        print ("Target is present in the list")
        print (list1)
    else:
        print ("Target is not present in the list")








