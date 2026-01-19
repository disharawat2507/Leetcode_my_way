# Given a cyclic linkedlist, find the length of the linkedlist.
# Approach: we will first find out the point where both slow and fast pointers are same, then we will call one method where we will pass slow, fast pointer . move fats pointer by one step, make counter as 1. then keep on iterating till slow again becimes equal to fast.
# simultaneously increase the counter. at the end return counter.
# Time complexity: O(n)
# Space complexity: O(1) because no space only using 2 pointers and 1 counter varriable

class Solution:
    def lengthofloop(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next    
            if slow == fast:
                return self.findlen(slow,fast)
        return 0  

    def findlen(self, slow,fast):
        count = 1
        fast = fast.next
        while fast != slow:
            count +=1
            fast = fast.next

        return count   
