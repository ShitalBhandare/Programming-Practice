'''
Problem Description
You are given an array citations where citations[i] represents the number of citations a researcher received for their i-th paper. Your task is to find and return the researcher's h-index.

The h-index is defined as the maximum value of h such that the researcher has published at least h papers that have each been cited at least h times.

For example, if a researcher has 5 papers with citations [3, 0, 6, 1, 5]:

They have 3 papers with at least 3 citations each (papers with 3, 6, and 5 citations)
They have 2 papers with at least 4 citations each (papers with 6 and 5 citations)
They have 2 papers with at least 5 citations each (papers with 6 and 5 citations)
They have only 1 paper with at least 6 citations (the paper with 6 citations)
The h-index would be 3 because the researcher has 3 papers with at least 3 citations each, but does not have 4 papers with at least 4 citations each.

'''

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Sort citations in descending order to check from highest to lowest
        citations.sort(reverse=True)
      
        # Try each possible h-index value from largest to smallest
        # h represents the potential h-index value we're testing
        for h in range(len(citations), 0, -1):
            # Check if the h-th paper (1-indexed) has at least h citations
            # citations[h-1] is the h-th paper when counting from 1
            # If the h-th paper has >= h citations, then all papers before it
            # also have >= h citations (since sorted in descending order)
            if citations[h - 1] >= h:
                return h
      
        # If no valid h-index found, return 0
        return 0
