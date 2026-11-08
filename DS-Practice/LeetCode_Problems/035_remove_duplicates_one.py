'''
The core goal of the Remove Duplicates from Sorted Array problem on AlgoMonster is to modify the array in-place so that each unique element appears only once, while maintaining their relative order. The function must return the count of unique elements (k)
Does not matter what you return beyond k/index
'''

def remove_duplicates(nums):
    if not nums:
        return 0
    
    # The first element is always unique, so start writing at index 1
    write_index = 1
    
    # Scan the array starting from the second element
    for i in range(1, len(nums)):
        # If the current element is different from the previous one, it's unique
        if nums[i] != nums[i - 1]:
            nums[write_index] = nums[i]
            write_index += 1
            
    return write_index
