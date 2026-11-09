'''
You are given an array nums of size n. Your task is to find and return the majority element in this array.

The majority element is defined as the element that appears more than ⌊n / 2⌋ times in the array. In other words, it's an element that occurs more than half the time in the array.

For example:

In an array of size 7, the majority element must appear at least 4 times
In an array of size 8, the majority element must appear at least 5 times
The problem guarantees that a majority element always exists in the given array, so you don't need to handle cases where no majority element is present.
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Find the majority element using Boyer-Moore Voting Algorithm.
        The majority element appears more than n/2 times in the array.

        Args:
            nums: List of integers

        Returns:
            The majority element
        """
        count = 0
        candidate = 0

        # Boyer-Moore Voting Algorithm
        for num in nums:
            if count == 0:
                # When count reaches 0, select current element as new candidate
                candidate = num
                count = 1
            else:
                # Increment count if current element matches candidate
                # Decrement count if current element differs from candidate
                if candidate == num:
                    count += 1
                else:
                    count -= 1

        # The candidate at the end is guaranteed to be the majority element
        # (given that a majority element exists as per problem constraints)
        return candidate

