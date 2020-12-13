'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        '''
        First we will add an auxiliary "dummy" node, which points to the list head. The "dummy" node is used to simplify some corner cases such as a list with only one node, or removing the head of the list. 
        '''
        
        dummy_node = ListNode(0)
        dummy_node.next = head
        
        fast_ptr = slow_ptr = prev = dummy_node
        walker = 0
        while walker < n:
            walker += 1
            fast_ptr = fast_ptr.next
        
        while fast_ptr != None:
            prev = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next

        prev.next = slow_ptr.next
        #slow_ptr.next = slow_ptr.next.next
            
        return dummy_node.next
        
        
'''
Space Complexity: O(1)
Time Complexity: O(n)
'''
