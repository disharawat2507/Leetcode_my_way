# LeetCode 700: Search in a Binary Search Tree
# Approach : we know that in BST, left value is always smaller than node/root and root is always smaller than its right values. So, here we are comparing the value of target with root's value and accordingly updating the root.
# Time Complexity : O(log n)
# Space Complexity : O(1) as i m using iterative approach

class Solution:
    def searchBST(self,root, target) :
        if root is None:
            return

        while root:
            if root.val > target:
                root = root.left
            elif root.val < target:
                root = root.right
            elif root.val == target:
                return root   
        return root                 
