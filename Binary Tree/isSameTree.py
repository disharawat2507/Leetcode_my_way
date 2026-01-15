# Leetcode 100: Same Tree
# Approach : we will check if each node of both the trees are same or not. If every node value is same , return true else false
# Time Complexity : O(n)
# Space Complexity : O(h1,h2). which ever height is small (h is the height of the tree)

class Solution :
    def isSameTree(self,root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2 or (root1.val != root2.val):
            return False

        return self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)
