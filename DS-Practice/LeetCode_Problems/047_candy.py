'''
There are n children standing in a line.

Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
'''

import array

def minCandy(arr):
    n = len(arr)

    leftcandy = array.array('i', [1] * n)
    rightcandy = array.array('i', [1] * n)

    # left pass
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            leftcandy[i] = leftcandy[i - 1] + 1

    # right pass
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            rightcandy[i] = rightcandy[i + 1] + 1

    # calculate final answer
    return sum(max(leftcandy[i], rightcandy[i]) for i in range(n))

if __name__ == "__main__":
    arr = array.array('i', [1, 2, 3, 4, 5 ])
    print(minCandy(arr))
