# Leetcode 1178 . Path to the target node from root.
# Approach : we use inorder traversal here. We will check if root val is not equal to the target node value. If value doesnot match, add it to the result array and return true. keep on looping on the same method with root.left or 
# root.right. if we reach the node which doesnot have left or right, jus remove that node. In the main method check if the helper method return True, if yes, return the result, else return blank array.
# Time Complexity : O(n). n is the  number of nodes
# Space Complexity : O(h), h is the height of tree

class Solution:
    def roottoleaf(self,root, target, res) :
        if root is None:
            return False
        res.append(root.val)    
        if root.val == target:
            return True
        if self.roottoleaf(root.left, target, res) or self.roottoleaf(root.right, target, res):
            return True
        res.pop()
        return False        


    def allRootToLeaf(self, root, target):
        res =[]
        if root is None:
            return []

        if self.roottoleaf(root,target,res):
            return res
        return []   
