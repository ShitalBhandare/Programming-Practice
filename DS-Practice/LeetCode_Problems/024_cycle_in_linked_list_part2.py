'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow_ptr = fast_ptr = ptr = head
        
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            
            if slow_ptr == fast_ptr:
                # Cycle Present
                while slow_ptr != ptr:
                    slow_ptr = slow_ptr.next
                    ptr = ptr.next
                
                return ptr
                
        return None

'''
Time Complexity: O(n
Space Complexity: O(1)
'''


==============

// Remove cycle/loop from the linked list

def remove_loop(self, slow, fast):
    if slow == fast:
        slow = self.head
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None
        return True

