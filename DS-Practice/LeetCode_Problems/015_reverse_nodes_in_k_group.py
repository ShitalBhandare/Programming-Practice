'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverse_list(self, head, k):
        
        prev = None
        current = head
        
        while k:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
            k -= 1
        
        return prev
        
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
         
        ptr = head
        newhead =None
        ktail = None
        count = 0
        
        while ptr:
            
            count = 0
            
            # Making head to current k nodes list head pointer
            head = ptr
            
            while ptr and count < k:
                ptr = ptr.next
                count += 1

            if count == k:

                revhead = self.reverse_list(head, k)

                # Head of the final list
                if not newhead:
                    newhead = revhead

                if ktail:
                    ktail.next = revhead

                ktail = head
                head = ptr
            
        if ktail:
            ktail.next = head
                
        return newhead if newhead else head
            
            
'''
Time Complexity: O(n)
Space Complexity: O(1)

'''
