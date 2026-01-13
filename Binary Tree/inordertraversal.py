# Inorder Traversal in Binary Tree.
# Approach : Inorder traversal goes Left, root and right. So we will always first check if root is not none. if not, we will go to extreme left, start printing and then move to right.
# Time Complexity : O(n)
# Space Complexity : O(h) best case where h is the height of the tree, worst is O(n) where tree is left skewed or right skewed.
  
class Solution:
    def inordertraversal(self, root):
        if root is None:
            return 
           
        self.inordertraversal(root.left)
        print(root.val) 
        self.inordertraversal(root.right) 
