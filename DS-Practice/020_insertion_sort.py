
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

'''
Time Complexity of Insertion Sort
Best case: O(n), If the list is already sorted, where n is the number of elements in the list.
Average case: O(n2), If the list is randomly ordered
Worst case: O(n2), If the list is in reverse order
Space Complexity of Insertion Sort
Auxiliary Space: O(1), Insertion sort requires O(1) additional space, making it a space-efficient sorting algorithm.
'''
