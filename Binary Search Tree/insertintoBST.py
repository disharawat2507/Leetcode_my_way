# Leetcode 701 : Insert to a binary search tree
# Approach : Iterate on binary tree to check where we can add the given value node. We know that in BST the left side is always smaller than the right side, so we will use that logic to traverse in the tree
# Time Complexity : O(h) , h is the height of the tree
# Space Complexity : O(1). since we are iterating on the tree

class Solution:
    def insertintoBST(self,root, value) :
        if root is None:
            node = TreeNode(val = value)
            return node

        curr = root
        while curr:
            if curr.val > value:
                if curr.left is None:
                    curr.left = TreeNode(val = value)
                    break
                else:
                    curr = curr.left
            elif curr.val < value:
                if curr.right is None:
                    curr.right = TreeNode(val = value)
                    break
                else:
                    curr = curr.right

        return root                            


        

