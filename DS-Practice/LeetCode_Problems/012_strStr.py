'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 
Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2


'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle:
            return 0
        elif needle in haystack:
            return haystack.index(needle)
        else:
            return -1

'''
Another approaches:

1) Linear time slice:
    - Traverse along the string and match substring of length L with needle.
    - If match found, return start index of substring

2) Two pointer: Linear time slice
    - Problem with above approach is it matches all the substring of length L with needle
    - Two pointer appraoch can be used
    - traverse along the haysack. check first character matches with first charcter of needle
    - If matches, check next len(L) characters one by one. If length matches, return index


Algorithm:

    Move pn till you'll find the first character of the needle string in the haystack.

    Compute the max string match by increasing pn, pL and curr_len in the case of equal characters.

    If you managed to get the full match, curr_len == L, return the start position of that match, pn - L.

    If you didn't, backtrack: pn = pn - curr_len + 1, pL = 0, curr_len = 0.


Time Complexity: O((N-L)L) L length substring and loop it in N-L+1 times. In worst case, O(N)
Space Complexity: O(1)
'''
