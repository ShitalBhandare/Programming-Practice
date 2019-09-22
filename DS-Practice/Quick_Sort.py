# This program implements the quick sort


def quick_sort(a, l, h):
    """
    :param a: List1
    :param l: Index 0
    :param h: Last index
    :return: sorted list
    """

    low = l + 1
    high = h
    pivot = a[l]

    while(low < high):
        while(low <= h and a[low] <= pivot):
            low += 1

        while(a[high] > pivot):
            high -= 1

        if low < high:
            temp = a[low]
            a[low] = a[high]
            a[high] = temp
            low += 1
            high -= 1

    a[l] = a[high]
    a[high] = pivot

    if l < high:
        quick_sort(a, l, high-1)

    if low < h:
        quick_sort(a, high + 1, h)

    return a




if __name__ == "__main__":
    n = int(input("Enter the no of elements:"))
    list1 = []
    for _ in range(n):
        list1.append(int(input("Enter the element:")))

    print (quick_sort(list1, 0, len(list1) - 1))
