# Leetcode 234. Palindrome Linked List
# Approach : We will take 2 pointer a move fast pointer at twice speed, so that when it reaches the end, the slow pointer is in the middle. Simulatneously we will storing the value of slow pointer in the stack.
# Once it reaches the end and still end node is not cover we will move the slow pointer by one step. Then check of palindrome will begin, it will move forward and we will pop elements from stack, if they are same then continue else return False.
# Time Complexity: O(n)
# Space Complecity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return
        stack =[]    
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        if stack:
            while slow is not None:
                if slow.val == stack.pop():
                    slow = slow.next
                else:
                    return False

        return True                         
