'''
Given a string s consisting of upper/lower-case alphabets and empty space characters ' ', return the length of the last word in the string. If the last word does not exist, return 0.

Examples:  

Input  : s = "Geeks For Geeks"
Output : 5
Explanation: length(Geeks)= 5

Input : s = "Start Coding Here"
Output : 4
Explanation: length(Here) = 4

Input  : s= " "
Output : 0

'''


'''
Naive approach
'''

def length_of_last_word(s: str) -> int:
    words = s.split()
    return len(words[-1]) if words else 0

# Examples
print(length_of_last_word("Hello World"))        # Output: 5
print(length_of_last_word("   fly me   to the moon  "))  # Output: 4
print(length_of_last_word("   "))               # Output: 0


'''
Efficient Approach
'''

# C++ program for the above approach

def lastWordLen(s):
    len1 = 0

    s = s.lstrip()
    s = s.rstrip()

    for i in range(len(s)):
        if s[i] == ' ':
            len1 = 0
        else:
            len1 += 1

    return len1


input_str = "Geeks For Geeks  "

print("The length of last word is",
      lastWordLen(input_str))
