# Leetcode 141. Linked List Cycle
# Approach : take 2 pointers, move the fast pointer twice and slow pointer once, if slow and fast are same at some point, return true, else return false
# Time Complexity : O(n) , n is the number of nodes
# Space Complexity : O(1) , no space used, moving 2 pointers

class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False  
