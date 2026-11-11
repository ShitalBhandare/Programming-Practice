'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Track the maximum index we can reach so far
        max_reachable = 0
      
        # Iterate through each position and its jump value
        for current_pos, jump_length in enumerate(nums):
            # If current position is beyond our maximum reach, we can't proceed
            if max_reachable < current_pos:
                return False
          
            # Update the maximum reachable index
            # Current position + jump length gives us the farthest we can go from here
            max_reachable = max(max_reachable, current_pos + jump_length)
      
        # If we've gone through all positions without getting stuck, we can reach the end
        return True
