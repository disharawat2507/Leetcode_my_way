# Leetcode 104
# Approach : always check if the root is None or not. If None, return 0. keep on calling method with root.left and root.right and then return 1 + max(left, right).
# Time Complexity : O(n)
# Space Complexity : O(h) , h is the height of the tree

class Solution:
    def maxhieght(self, root):
        if root is None:
            return 0

        left = self.maxheight(root.left)
        right = self.maxheight(root.right)

        return 1 +max(left, right)  
