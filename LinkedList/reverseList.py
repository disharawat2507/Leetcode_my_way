# Leetcode 206: Reverse Linked List
# Approach: we will use the 3 pointer approach to reverse the linkedlist. prev, next and curr. keep on giving their values to each other and finaaly return the previous. 
# Time Complexity: O(n)
# Space Complexity : O(1), we are not using any space just modifiying the original linkedlist.

class Solution:
    def reverseList(self, head):
        prev = None
        if not head or not head.next:
            return head

        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev    
