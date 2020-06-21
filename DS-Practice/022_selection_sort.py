
# This program implements selection sort

def selection_sort(list1, last):

    current = 0
    while(current < last):
        smallest = current
        walker = current + 1

        while(walker < last):
            if list1[walker] < list1[smallest]:
                smallest = walker
            walker += 1

        temp = list1[smallest]
        list1[smallest] = list1[current]
        list1[current] = temp

        current += 1

    print (list1)


if __name__ == "__main__":
    n = int(input("Enter the no of elements:"))
    list1 = []
    for _ in range(n):
        list1.append(int(input("Enter the element:")))

    selection_sort(list1, len(list1))