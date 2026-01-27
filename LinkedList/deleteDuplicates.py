# Leetcode 83. Remove Duplicates from Sorted List
# Approach : since the linkedlist is sorted, everytime we have to check if the node and its next node values are same or not. If same, change its next value to next.next else, make the next node as current node.
# Time Complexity : O(n)
# Space Complexity: O(1) we are just using one pointer to iterate on the linkedlist and one dummy node. we are just rearranging the linkedlist.
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        curr = head
        dummy = ListNode(val = -1)
        dummy.next = head
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next  
