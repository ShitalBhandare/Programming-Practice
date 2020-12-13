'''
Problem Statement:
    Write a program to find the node at which the intersection of two singly linked lists begins.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        if not headA or not headB:
            return None

        walkerA, walkerB = headA, headB
        lenA, lenB = 0, 0
        while walkerA:
            lenA += 1
            walkerA = walkerA.next
        while walkerB:
            lenB += 1
            walkerB = walkerB.next
        diff = abs(lenA - lenB)
        walkerA, walkerB = headA, headB
        if lenA > lenB:
            while diff > 0:
                walkerA = walkerA.next
                diff -= 1
        else:
            while diff > 0:
                walkerB = walkerB.next
                diff -= 1

        while walkerA and walkerB:
            if walkerA == walkerB:
                return walkerA
            walkerA = walkerA.next
            walkerB = walkerB.next
        return None


'''
Space Complexity: O(1)
Time Complexxity: O(n)
'''
