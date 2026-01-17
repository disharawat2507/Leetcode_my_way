# Leetcode 230: Kth Smallest Element in a BST
# Approach : keep a stack . iterate on root node and move till left most node. then start poping elemnents from the stack and decrease the value of k. once k reaches 0, return the node which just poped out.
# Time Complexity : O(H + k)
# Space Complexity: O(H)


class Solution:
    def kthSmallest(self, root, k):
        stack = []
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val

            curr = curr.right
