
# This is program to implement bubble sort


def bubble_sort(list1, last):

    current = 0
    sorted = False

    while (current < last and sorted is False):
        sorted = True
        walker = last - 1

        while(walker > current):
            if list1[walker] < list1[walker-1]:
                sorted = False
                temp = list1[walker]
                list1[walker] = list1[walker-1]
                list1[walker-1] = temp
            walker -= 1

        current += 1

    print (list1)

if __name__ == "__main__":
    n = int(input("Enter the no of elements:"))
    list1 = []
    for _ in range(n):
        list1.append(int(input("Enter the element:")))

    bubble_sort(list1, len(list1))