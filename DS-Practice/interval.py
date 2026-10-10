'''
Given a set of time intervals in any order, merge all overlapping intervals into one and output the result which should have only mutually exclusive intervals.
Ans. Merge all overlapping intervals from a given list of intervals to produce mutually exclusive intervals.
'''

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

'''
Time Complexity
O(n log n) due to sorting of the intervals, where n is the number of intervals.

Space Complexity
O(n) to hold the merged intervals list in the worst case where no intervals overlap.
'''
