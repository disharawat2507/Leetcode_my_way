# Leetcode 160. Intersection of Two Linked Lists
# Approach: use 2 pointers, keep on moving one pointer till it is not None and if None move to the head of second linkedlist, do the same with both heads. at the end there will be a point where either both pointers will be on same
# node or None.
# Time Complexity: O(n+m) , n, m are the number of nodes in both linkedlist
# Space Complexity: O(1) , no extra space used, only using 2 pointers approach.

class Solution:
    def getIntersectionNode(self, headA, headB):
        pa = headA
        pb = headB

        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA

        return pa   
