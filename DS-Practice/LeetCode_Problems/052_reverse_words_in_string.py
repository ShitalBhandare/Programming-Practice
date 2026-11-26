'''
Reverse word order

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

'''

def reverse_words(s: str) -> str:
    return " ".join(s.split()[::-1])

'''
Reverse each word in place (keeping word order)
'''

def reverse_each_word(s: str) -> str:
    return " ".join(word[::-1] for word in s.split())

