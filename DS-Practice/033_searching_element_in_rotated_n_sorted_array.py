'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# program to search element in rotated and sorted array

# Approach: Use modified binary search to solve this in O(log n) time complexity


def mod_bin_search(arr, begin, end, key):
    
    if begin > end:
        return -1
        
    mid = (begin+end)//2
    #print(mid)
    
    if arr[mid] == key:
        return mid
        
    if arr[begin] <= arr[mid]:
        
        if key >= arr[begin] and key <= arr[mid]:
            return mod_bin_search(arr, begin, mid -1 , key)
        else:
            return mod_bin_search(arr, mid + 1, end, key)
            
    else:
        
        if key >= arr[mid] and key <= arr[end]:
            return mod_bin_search(arr, mid + 1, end, key)
            
        else:
            return mod_bin_search(arr, begin, mid - 1, key)


if __name__ == "__main__":
    arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    key = 5
    size = len(arr) - 1
    
    index = mod_bin_search(arr, 0, size, key)
    if index == -1:
        print("Key is not present in the given array")
    else:
        print("Key is present at index", index)
    


