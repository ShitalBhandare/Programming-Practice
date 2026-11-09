'''
Problem Description
You are given an integer array nums that is sorted in non-decreasing order. Your task is to remove duplicates from this array in-place such that each unique element appears at most twice. The relative order of elements must be preserved.

The key requirements are:

Modify the array in-place (cannot create a new array)
Use only O(1) extra memory
Each unique number can appear at most 2 times
Return the length k of the modified array
The first k elements of nums should contain the final result
For example:

If nums = [1,1,1,2,2,3], after removing duplicates where each element appears at most twice, the array becomes [1,1,2,2,3,_] where _ represents any value (doesn't matter). The function should return k = 5.
'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Pointer to track the position for the next valid element
        write_index = 0
      
        # Iterate through each element in the array
        for current_num in nums:
            # Allow element if:
            # 1. We have less than 2 elements (write_index < 2), OR
            # 2. Current element is different from the element 2 positions back
            if write_index < 2 or current_num != nums[write_index - 2]:
                # Place the current element at the write position
                nums[write_index] = current_num
                # Move write pointer forward
                write_index += 1
      
        # Return the length of the modified array
        return write_index
