'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

 
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1


'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        '''
        Brute Force Approach:
        Time Complexity: O(n)
        Space Complexity: O(1)

        for i in range(len(nums)):
            if nums[i] < target:
                continue
            else:
                return i

        return len(nums)

        '''

        '''
        Binary Search Approach:
        Time Complexity: O(log(n))
        Space Complexity: O(1)
        '''

        start = 0
        end = len(nums) - 1

        while (start <= end):
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return start
