'''
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
'''


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(sqrt(x))
