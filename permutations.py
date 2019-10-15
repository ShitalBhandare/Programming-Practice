

'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

'''
Get largest no from given array
Method 1: Comparison based sorting
Method 2: Using permutations module of itertools
'''


from itertools import permutations

def find(list1):
    lst = []
    for i in permutations(list1, len(list1)):
        lst.append("".join(map(str, i)))
    print(max(lst))

list1 = [23, 87, 93, 20]
find(list1)


Output:

93872320