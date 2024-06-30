'''

Given a boolean 2D array, where each row is sorted. Find the row with the maximum number of 1s.

Example:

Input matrix :          0 1 1 1
                        0 0 1 1
                        1 1 1 1  // this row has maximum 1s
                        0 0 0 0
Output: 2
'''

def findLowerBound(row, low, high, searchkey):

    ans = high - 1 # or keep at 0
    while low <= high:
        mid = (low + high)//2
        if mid >= searchkey:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def findMax1s(arr, column_size):
    
    size = len(arr)
    count_max = 0
    count_index = -1

    for i in range(size):
        c_max = column_size - findLowerBound(arr[i], 0, column_size-1, 1)
        if c_max > count_max:
            count_max = c_max
            count_index = i

    return count_index





