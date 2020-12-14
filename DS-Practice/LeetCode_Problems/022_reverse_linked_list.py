'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        '''
        # Approch 1: Iterative

        current = head
        prev = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
        '''

        # Approach 2: Recursive
        '''
        if not head:
            return

        first = head
        rest = first.next

        if not rest:
            head = first  => Need to check how leetcode has defined list head
            return head

        self.reverseList(rest)
        first.next.next = first
        first.next = None
        '''

        if not head or not head.next:
            return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p


'''
Iterative:
    Time Complexity: O(n)
    Space Complexity: O(1)

Recursive:
    Time Complexity: O(n)
    Space Complexity: O(n) => for storing recursive call stacks

'''

