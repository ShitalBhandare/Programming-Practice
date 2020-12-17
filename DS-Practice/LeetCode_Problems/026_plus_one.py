'''
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
'''


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        len_digits = len(digits)
        for i in range(len_digits, 0, -1):
            index = i - 1

            if digits[index] == 9:
                digits[index] = 0
            else:
                digits[index] += 1

                return digits

        return [1] + digits
