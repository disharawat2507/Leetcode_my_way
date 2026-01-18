# Leetcode 19: Remove Nth Node From End of List.
# Approach: We will take 2 pointers slow and fast .Dummy listnode is created for the edge case when head is needed to be removed. so evenif head is removed we are returning dummy.next, which will give us the required result.
# Then, we will move fast node to n steps and slow node to dummy still. now till fast.next exists, we will keep moving fast n slow by 1 step. once fast reaches end, slow is just before the node to be deleted. so, we connect 
# slow.next to slow.next.next so that if there are any nodes after the to be deleted node, they are also connected.
# Time Complexity : O(n)
# Space Complexity: O(1). No extra space needed. just using 2 pointers approach


class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        while n>0:
            fast = fast.next
            n -= 1
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return dummy.next
