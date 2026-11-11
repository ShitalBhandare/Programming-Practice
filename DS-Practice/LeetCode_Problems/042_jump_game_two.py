'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        # Initialize variables
        jump_count = 0  # Number of jumps made
        current_jump_end = 0  # The farthest index reachable with current number of jumps
        farthest_reachable = 0  # The farthest index we can reach overall
      
        # Iterate through all elements except the last one
        # We don't need to check the last element since we want to reach it, not jump from it
        for i in range(len(nums) - 1):
            # Update the farthest index we can reach from current position
            farthest_reachable = max(farthest_reachable, i + nums[i])
          
            # If we've reached the end of the current jump's range
            if i == current_jump_end:
                # We must make another jump
                jump_count += 1
                # Update the range of the next jump to the farthest we can reach
                current_jump_end = farthest_reachable
      
        return jump_count



