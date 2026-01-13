# Preorder Traversal in Binary Tree.
# Approach : This is preorder traversal. It follow Root, Left, Right. We are iterating on the tree. Everytime we check if root is none, return , else we will print the value following the traversal order. 
# Time Complexity : O(n)
# Space Complexity : O(h) . where h is the height of the tree. worst case will be if all the nodes are on left or right side, it will be O(n).

class Solution:
    def preordertraversal(self, root):
        if root is None:
            return 
        print(root.val)    
        self.preordertraversal(root.left)
        self.preordertraversal(root.right) 
