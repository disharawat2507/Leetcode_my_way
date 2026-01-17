# LeetCode 98: Validate Binary Search Tree
# Approach : In the starting of the question we will take min and max values as + float('inf') and -float(inf). iterate over the helper method where we check if there is any value in left which is greater than the max value 
#   or if there is any value in the right which is smaller than the right side value. If yes, return False because it disqualifies condition for BST else return True.
# Time Complexity : O(n)
# Space Complexity : O(h) . h is the height of the tree. It is used by recurssion stack 

class Solution:
    def helpermethod(self, root,minval,maxval):
        if root is None:
            return True
        if (root.val >= maxval or root.val <= minval):
            return False
        return  self.helpermethod(root.left, minval,root.val) and self.helpermethod(root.right, root.val,maxval)   
    def isValidBST(self,root):
        return self.helpermethod(root,-float('inf'), float('inf'))
