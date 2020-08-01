'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


'''



class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse_num = str(x)[::-1]
        if x < 0:
            reverse_num = '-' + reverse_num[:len(reverse_num)-1]
    
        reverse_num = int(reverse_num)
        if reverse_num < pow(-2, 31) or reverse_num > pow(2, 31) - 1:
            return 0
        else:
            return reverse_num
