# Leetcode 876 Middle of the Linked List
# Approach : If head is not there, the is no middle node, so return. Take 2 pointers, slow and fast. Slow will take one step and fast will take 2 steps. so when the fast reaches the end, slow will be in the middle.
# Time Complexity : O(n)  
# Space Complexity : O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next    

        return slow    
