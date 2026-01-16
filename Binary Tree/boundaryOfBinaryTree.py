# Leetcode 545 Boundary of Binary Tree.
# Approach : Find all the leftmost nodes. Add them to the result. find all the leaf nodes, add them as well. Find all the right nodes, add them to results in reverse direction. for right and left boundary always check if the
# node is not leaf as we are adding leaf nodes separately. return the list at the end.
# Time Complexity: O(n)
# Space Complexity : O(n)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isleaf(self,root):
        return root.left is None and root.right is None
    def leftboundary(self,root, res):
        curr = root.left
        while curr:
            if not self.isleaf(curr):
                res.append(curr.val)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

    def rightboundary(self,root,res):
        curr = root.right
        temp =[]
        while curr:
            if not self.isleaf(curr):
                temp.append(curr.val)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left 
        res.extend(temp[::-1])            

    def addleaves(self, root, res):
        if self.isleaf(root):
            res.append(root.val)
            return
        if root.left:
            self.addleaves(root.left, res)
        if root.right:
            self.addleaves(root.right, res)        

    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        res =[]
        if root is None:
            return
        if not self.isleaf(root):
            res.append(root.val)    
        
        self.leftboundary(root,res) 
        self.addleaves(root, res)
        self.rightboundary(root,res)
        return res
