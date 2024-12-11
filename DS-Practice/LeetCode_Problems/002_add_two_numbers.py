'''
Problem statement:

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.


'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        l3 = ListNode(0)
        l4 = l3
        while l1 or l2:
            
            op1 = l1.val if l1 else 0
            op2 = l2.val if l2 else 0
            sum = op1 + op2 + carry
            carry = sum // 10
            
            l3.next = ListNode(sum % 10)
            l3 = l3.next
            
            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next 
        
        if carry > 0:
            l3.next = ListNode(carry)
            
        return l4.next
    
==================

'''

Program when numbers are not stored in reverse order but in correct order.

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def addNumbers(head1, head2):
    # Reverse both linked lists
    head1 = reverseList(head1)
    head2 = reverseList(head2)
    
    carry = 0
    dummy = ListNode(0)
    current = dummy
    
    # Add the two numbers
    while head1 or head2 or carry:
        val1 = head1.val if head1 else 0
        val2 = head2.val if head2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        
        if head1:
            head1 = head1.next
        if head2:
            head2 = head2.next
    
    # Reverse the result linked list
    return reverseList(dummy.next)

