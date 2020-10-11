'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = nums1 + nums2
        sorted_array = sorted(merged_array)
        mid = len(sorted_array) // 2
        if len(sorted_array) % 2 != 0:
            res = "{:.5f}".format(sorted_array[mid])
        else:
            sum = sorted_array[mid-1] + sorted_array[mid]
            res = "{:.5f}".format(sum/2)

        return float(res)/1.0
    
'''
Brute force solution
Time and space complexity: O(m+n)
m, n => length of list a and list b


Optimized appraoch using binary search will give o(log(m+n))
'''
