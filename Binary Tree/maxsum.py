# Leetcode 124: Binary Tree Maximum Path Sum.
# Approach : here we are calculating left sum and right sum of all nodes including itself.And finding what is the maximum sum using maxlen varriable. Finally returning the maxlen.
# Time Complexity : O(n). n is the number of nodes
# Space Complexity : O(h) . h is the height of binary tree


class Solution :
    def mainsolution(self,root):
        maxlen = [float('-inf')]
        self.maxsum(maxlen,root)
        return maxlen[0]

    def maxsum(self, maxlen,root) :
        if root is None:
            return 0
        left = max(0,self.maxsum(maxlen,root.left))
        right = max(0,self.maxsum(maxlen,root.right))  
        maxlen[0] = max(maxlen[0], left+right+root.val)  
        return root.val + max(left,right)
