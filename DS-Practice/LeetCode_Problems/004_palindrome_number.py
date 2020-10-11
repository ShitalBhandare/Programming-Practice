'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False
        else:
            orig_num = x
            rev_num = 0

            while (x > 0):
                rev = x % 10
                x = x / 10
                rev_num = rev_num * 10 + rev

            if orig_num == rev_num:
                return True
            else:
                return False
            

'''
Another appraoch is reverse only half of number and compare it with other half.
        int revertedNumber = 0;
        while(x > revertedNumber) {
            revertedNumber = revertedNumber * 10 + x % 10;
            x /= 10;
        }

        // When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
        // For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
        // since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.
        return x == revertedNumber || x == revertedNumber/10;
    }
}

'''
