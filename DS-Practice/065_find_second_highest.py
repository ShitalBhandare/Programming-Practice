'''
Given an array of numbers, find the second highest number in the array.
'''

def find_second_highest(arr):
    if len(arr) < 2:
        return None  # Or throw an error: array is too small

    highest = float('-inf')
    second_highest = float('-inf')

    for num in arr:
        if num > highest:
            second_highest = highest
            highest = num
        elif num > second_highest and num != highest:
            second_highest = num

    # Handle cases where no distinct second highest exists (e.g., [10, 10, 10])
    return second_highest if second_highest != float('-inf') else None

# Example usage:
print(find_second_highest([12, 35, 1, 10, 34, 1]))  # Output: 34
