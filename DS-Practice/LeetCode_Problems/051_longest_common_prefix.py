'''
Given an array of strings arr[], return the longest common prefix among each and every strings present in the array. If there’s no prefix common in all the strings, return “”.

Examples:

Input: arr[] = [“geeksforgeeks”, “geeks”, “geek”, “geezer”]
Output: “gee”
Explanation: “gee” is the longest common prefix in all the given strings: “geeksforgeeks”, “geeks”, “geeks” and “geezer”.
'''


def longestCommonPrefix(arr):

    # Find length of smallest string
    minLen = len(arr[0])

    for s in arr:
        minLen = min(minLen, len(s))

    res = []
    for i in range(minLen):

        # Current character (must be the same
        # in all strings to be a part of result)
        ch = arr[0][i]

        for s in arr:
            if s[i] != ch:
                return "".join(res)

        # Append to result
        res.append(ch)

    return "".join(res)


if __name__ == "__main__":
    arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
    print(longestCommonPrefix(arr))
