'''
You are given an integer array nums and a non-negative integer k. Your task is to rotate the array to the right by k steps.

When rotating an array to the right by k steps, each element moves k positions to the right. Elements that go beyond the last position wrap around to the beginning of the array.

For example:

If nums = [1, 2, 3, 4, 5, 6, 7] and k = 3
After rotating right by 3 steps, the array becomes [5, 6, 7, 1, 2, 3, 4]
The last 3 elements [5, 6, 7] moved to the front
The first 4 elements [1, 2, 3, 4] shifted to the right
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate the array to the right by k steps in-place.
      
        Args:
            nums: The input array to be rotated
            k: Number of steps to rotate right
      
        Returns:
            None (modifies array in-place)
        """
        def reverse(start: int, end: int) -> None:
            """
            Reverse elements in nums from index start to end (inclusive).
          
            Args:
                start: Starting index of the subarray to reverse
                end: Ending index of the subarray to reverse
            """
            while start < end:
                # Swap elements at start and end positions
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
      
        n = len(nums)
        # Handle cases where k > n by taking modulo
        k = k % n
      
        # Step 1: Reverse the entire array
        reverse(0, n - 1)
      
        # Step 2: Reverse the first k elements
        reverse(0, k - 1)
      
        # Step 3: Reverse the remaining n-k elements
        reverse(k, n - 1)
