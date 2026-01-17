# Leetcode 450 Delete Node in a BST
# Approach : In a BST, every node's left child is smaller and its right child is larger. When the key matches a node, we remove that node and replace it with its right subtree.
# We then take the entire left subtree and attach it to the leftmost node of that right subtree
# Time Complexity : O(H), H is the height of the tree
# Space Complexity : O(1)

class Solution:
    def helpermethod(self, root):
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        left_child = root.left
        rightchild= root.right

        while rightchild.left :
            rightchild = rightchild.left
        rightchild.left = left_child
        return root.right            

    def deleteNode(self,root, key) :
        if root is None:
            return
        if root.val == key:
            return self.helpermethod(root)

        curr = root
        while curr:
            if curr.val > key:
                if curr.left and curr.left.val == key:
                    curr.left =  self.helpermethod(curr.left)
                    break
                else:
                    curr = curr.left
            if curr.val < key:
                if curr.right and curr.right.val == key:
                    curr.right = self.helpermethod(curr.right)
                    break
                else:
                    curr = curr.right

        return root 
