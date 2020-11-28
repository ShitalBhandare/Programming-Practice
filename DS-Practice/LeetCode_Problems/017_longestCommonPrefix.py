'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        longestCommonPrefix = ""
        for commonPrefix in zip(*strs):
            if len(set(commonPrefix)) == 1:
                longestCommonPrefix += commonPrefix[0]
            else:
                break
        return longestCommonPrefix


'''
The purpose of zip() is to map the similar index of multiple containers so that they can be used just using as single entity.
'''

