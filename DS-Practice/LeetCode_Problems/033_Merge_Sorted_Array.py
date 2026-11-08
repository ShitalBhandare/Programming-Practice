'''
Problem Description
You have two sorted integer arrays nums1 and nums2 that are already arranged in non-decreasing order. You also have two integers m and n that tell you how many valid elements are in nums1 and nums2 respectively.

Your task is to merge nums2 into nums1 so that nums1 becomes one sorted array containing all elements from both arrays.

Here are the key requirements:

nums1 has a total length of m + n to accommodate all elements
The first m positions in nums1 contain the valid elements to be merged
The last n positions in nums1 are filled with zeros and serve as placeholder space
nums2 has length n and contains n valid elements
The merge must be done in-place - you need to modify nums1 directly rather than creating a new array
The final result should have all elements sorted in non-decreasing order
For example, if nums1 = [1,2,3,0,0,0] with m = 3 and nums2 = [2,5,6] with n = 3, after merging, nums1 should become [1,2,2,3,5,6].
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge two sorted arrays in-place.
        nums1 has enough space to hold elements from both arrays.

        Args:
            nums1: First sorted array with extra space at the end
            m: Number of valid elements in nums1
            nums2: Second sorted array to merge into nums1
            n: Number of elements in nums2
        """
        # Start from the end of the merged array
        write_index = m + n - 1

        # Pointers to the last valid elements in each array
        nums1_index = m - 1
        nums2_index = n - 1

        # Continue until all elements from nums2 are processed
        while nums2_index >= 0:
            # If nums1 still has elements and current element is larger than nums2's
            if nums1_index >= 0 and nums1[nums1_index] > nums2[nums2_index]:
                # Place the larger element from nums1 at the current position
                nums1[write_index] = nums1[nums1_index]
                nums1_index -= 1
            else:
                # Place the element from nums2 (either it's larger or nums1 is exhausted)
                nums1[write_index] = nums2[nums2_index]
                nums2_index -= 1

            # Move the write position one step back
            write_index -= 1
