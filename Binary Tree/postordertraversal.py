Post Order Traversal.
Approach : Postorder traversal in binary trees follows left, right , root. We always check if the value comming is not null. If true , we traverse first to left, then to right n then to root.
Time Complexity : O(n)
Space Complexity : O(h) where h is the height of the tree. In the worst case (a skewed tree), this is O(n); in a balanced tree, it is O(log n)

class Solution:
    def postordertraversal(self, root):
        if root is None:
            return 
           
        self.postordertraversal(root.left) 
        self.postordertraversal(root.right)  
        print(root.val)  
