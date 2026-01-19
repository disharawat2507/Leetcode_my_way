# Leetcode 203. Remove Linked List Elements
# Approach: make a dummy list and return dummy.next , it will cover the edge case where the head needs to be remove. There is a check where we always see the next element have the target value or not. if yes, make connection
# to next.next node, else move curr to next node.
# Time complexity : O(n)
# Space complexity: O(1)

# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def deleteAllOccurrences(self, head, target):
        dummy = ListNode(val = -1)
        dummy.next = head
        curr = dummy
        while curr and curr.next:
            if curr.next.val == target:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next        

