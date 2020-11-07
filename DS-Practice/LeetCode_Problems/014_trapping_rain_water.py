'''
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
'''


class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        result = 0

        while left < right:
            if left_max < right_max:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    result += left_max - height[left]
                    left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    result += right_max - height[right]
                    right -= 1

        return result

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''

