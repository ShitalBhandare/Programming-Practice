
# This is the program for insertion sort

def insertion_sort(list1, last):

    current = 1
    while(current < last):
        temp = list1[current]
        walker = current - 1
        while(temp < list1[walker] and walker >= 0):
            list1[walker + 1] = list1[walker]
            walker = walker - 1
        list1[walker + 1] = temp
        current = current + 1
    print (list1)


if __name__ == "__main__":
    n = int(input("Enter the no of elements:"))
    list1 = []
    for _ in range(n):
        list1.append(int(input("Enter the element:")))

    insertion_sort(list1, len(list1))