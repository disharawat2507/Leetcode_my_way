# Leetcode 86. Partition List
# Approach : we create 2 dummy linkedlist. Use 1 for storing all the values lesser than the target, use another for all others. Then at the end, the tail linkedlist should end with None. And this tail linkdlist should be 
# added to the next of head linkedlist. Finally return the head of the linkedlist
# Time Complexity : O(n)
# Space Complexity: O(1)

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummynode = ListNode(val = -1)
        dummynode2 = ListNode(val = -1)
        head1 = dummynode
        tail1 =dummynode2
        curr = head
        while curr:
            if curr.val < x:
                head1.next = curr
                head1 = head1.next
            else:
                tail1.next = curr
                tail1 = tail1.next    
            curr = curr.next
        tail1.next = None
        head1.next = dummynode2.next

        return dummynode.next 
