'''
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length. => This is very important statement.
That's why, we are just swapping the element in below code and not actually removing it.

'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        pointer1 = 0
        pointer2 = 1
        while pointer2 < len(nums):
            if nums[pointer1] != nums[pointer2]:
                pointer1 += 1
                nums[pointer1]  = nums[pointer2]
            pointer2 += 1

        return pointer1 + 1

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''

