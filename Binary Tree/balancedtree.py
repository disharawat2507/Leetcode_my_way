# Leetcode 110. Balanced tree check
# Approach: If the tree is not balanced, helper method will return -1 else some integer value. In helper method , we will try to find out the length of the tree, the left tree or right tree is -1 , return -1 or 
# abs(left - right) > 1, then return -1, else return the integer(height of the tree.) 
# Time Complexity : O(n)
# Space Complexity : O(h) where h is the height of the tree.

class Solution:
    def mainmethod(self,root):
        return self.balancedtree(root) != -1

    def balancedtree(self, root):
        if root is None:
            return 0

        left = self.balancedtree(root.left)
        if left == -1:
            return -1
        right = self.balancedtree(root.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1    

        return 1 +max(left, right)   
