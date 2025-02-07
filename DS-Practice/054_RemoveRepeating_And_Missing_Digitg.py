
'''
Given an unsorted array of size n. Array elements are in the range of 1 to n. 
One number from set {1, 2, …n} is missing and one number occurs twice in the array. Find these two numbers.
'''

def removeRepeatingAndMissingDigit(arr):
    n = len(arr)
    visited = [False] * (n+1)
    missing = -1
    repeating = -1
    for i in range(n):
        if visited[arr[i]]:
            repeating = arr[i]
        else:
            visited[arr[i]] = True

    for i in range(n+1):
        if not visited[arr[i]]:
            missing = arr[i]
            break

    print("Missing:", missing)
    print("Repeating:", repeating)
