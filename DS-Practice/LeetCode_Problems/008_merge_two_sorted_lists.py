'''
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4


No need to create 3rd list. Instead existing 2 lists need to be modified.

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        prehead = ListNode(-1)
        
        prev = prehead
        
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
                
            else:
                prev.next = l2
                l2 = l2.next
                
            prev = prev.next
            
        prev.next = l1 if l1 else l2
            
        return prehead.next

'''
Time Complexity: O(m+n) => m, n is length of l1 and l2 respectively
Space Complexity: O(1)
'''
