# This program implements Shell Sort

def shell_sort(list1, last):

    k = last / 2
    while(k > 0):
        current = k
        
        while(current < last):
            hold = list1[current]
            walker = current - k
            
            while(walker >= 0 and hold < list1[walker]):
                list1[walker + k] = list1[walker]
                walker = walker - k
                
            list1[walker + k] = hold
            current += 1
            
        k = k / 2

    print(list1)

if __name__ == "__main__":
    n = int(input("Enter the no of elements:"))
    list1 = []
    for _ in range(n):
        list1.append(int(input("Enter the element:")))

    shell_sort(list1, len(list1))
