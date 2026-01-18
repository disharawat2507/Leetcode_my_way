# Leetcode 2. Add Two Numbers
# Approach : Iterate on head1, head2 or carry, if any present. keep on adding the value everytime with each other. carry is quotient while node value is the remainder. Create a temp node and keep on adding new nodes to its
# next. At the end, return the dummy's next. 
# Time Complexity : O(n) , n is the number of nodes
# Space Complexity : O(n), number of nodes formed while summing 2 linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val = -1)
        temp = dummy
        t1 = l1
        t2 = l2
        carry = 0
        while t1 or t2 or carry:
            sumn = 0
            if t1:
                sumn += t1.val
                t1 = t1.next
            if t2:
                sumn += t2.val
                t2 = t2.next

            sumn += carry
            carry = sumn // 10
            node = ListNode(val = sumn%10)
            temp.next = node
            temp = temp.next

        return dummy.next    

