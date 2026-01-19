# Leetcode 2095. Delete the Middle Node of a Linked List
# Approach: use slow and fast pointer concept and at the very begining make fast as 1 step ahead and then till fast and fast.next, move fast pointer by 2 steps and slow pointer by 1 step. This will make slow pointer to stop just before the node to be removed
# make slow.next = slow.next.next . this will join the slow pointer after the node to be removed.
# Time complexity : O(n)
# Space complexity: O(1) , no space, just 2 pointers

class Solution:
     def deleteMiddle(self, head):
        if not head or not head.next:
            return None

        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return head 
