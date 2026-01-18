# Leetcode 328. Odd Even Linked List
# Approach : We are making odd as head and even as head.next. odd number will be the next of even number and even number will be next of odd number. we have used this approach to solve the problem.
# Time Complexity : O(n)
# Space Complexity : O(1) since we are modifying the same linkedlist

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        evenhead = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenhead
        return head        
        
