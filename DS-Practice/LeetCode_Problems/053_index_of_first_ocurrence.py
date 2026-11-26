'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

# Solution 1
text = "Hello, world!"
print(text.index("world"))


# Solution 2
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        haystack_length = len(haystack)
        needle_length = len(needle)

        if needle_length > haystack_length:
            return -1

        for start_index in range(haystack_length - needle_length + 1):
            if haystack[start_index:start_index + needle_length] == needle:
                return start_index

        return -1
