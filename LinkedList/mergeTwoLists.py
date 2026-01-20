# Leetcode 21. Merge Two Sorted Lists
# Approach : iterate on both the nodes and in the result listnode keep on adding the next nodes value.
# Time Complexity : O(n)
# Space complexity : O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        res = ListNode(val = -1)
        dummy = res
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    dummy.next = l1
                    l1 = l1.next
                else:
                    dummy.next = l2
                    l2 = l2.next
            elif l1:
                dummy.next = l1
                l1 = l1.next
            elif l2:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        return res.next  
