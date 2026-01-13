# Leetcode 160 Intersection of Two Linked Lists
# Approach : create 2 sets, iterate on each linkedlist one by one and keep on adding the nodes in one hashset. then iterte on other linkedlist and check if the node is already present in the previous set.
#   If yes, return that node, else return
# Time Complexity : O(n.m) where n, m are the number of nodes in both the linked list
# Space Complexity : O(n.m) where n, m are the number of nodes in both the linked list



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a1haset =set()
        b1hashset = set()

        if not headA or not headB:
            return null

        while headA:
            if headA not in a1haset:
                a1haset.add(headA)
            headA = headA.next

        while headB:
            if headB in a1haset:
                return headB
            else:
                b1hashset.add(headB)
            headB = headB.next

        return   
