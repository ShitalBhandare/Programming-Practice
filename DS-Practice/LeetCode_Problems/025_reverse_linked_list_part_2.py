'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL


'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        if not head:
            return
        
        prev = None
        current = head
        
        while m > 1:
            prev = current
            current = current.next
            m, n = m - 1, n - 1
           
        tail, con = current, prev
        while n:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            n -= 1
   
        if con:
            con.next = prev
        else:
            head = prev
        
        tail.next = current
            
        return head

            
'''
Time Complexity: O(n)
Space Complexity: O(1)
'''
