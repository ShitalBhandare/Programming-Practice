'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        '''
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        return sorted(nums)
        '''

        # Two pointer technique
        result = []
        nums_len = len(nums)
        i, j = 0, 0 # positive, negative

        while i < nums_len and nums[i] < 0:
            i += 1

        j = i - 1
        while j >= 0 and i < nums_len:
            if nums[j] * nums[j] < nums[i] * nums[i]:
                result.append(nums[j] * nums[j])
                j -= 1
            else:
                result.append(nums[i] * nums[i])
                i += 1

        while j >= 0:
            result.append(nums[j] * nums[j])
            j -= 1

        while i < nums_len:
            result.append(nums[i] * nums[i])
            i += 1

        return result

'''
Time Complexity: O(n)
Space Complexity: O(n)
'''

