'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# Python program to find maximum contiguos sum subarray


def find_max_subarray_sum(arr, size):
    
    max_so_far = 0
    max_ending_here = 0
    
    begin = 0
    end = 0
    s = 0
    
    
    for i in range(size):
        
        max_ending_here += arr[i]
        
        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1 
            
        elif max_ending_here > max_so_far:
            max_so_far = max_ending_here
            begin = s
            end = i
            
    print("\nMaximum Contiguous Subarray Sum:", max_so_far)
    print("\nBegin Index:", begin)
    print("\nEnd Index:", end)

if __name__ == "__main__":
    
    #arr = [-2, 3, -5, 4, 8, -6, 1, -9]
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    size = len(arr)
    
    find_max_subarray_sum(arr, size)
    
    
