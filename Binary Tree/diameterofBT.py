# Leetcode 543: Diameter of Binary Tree
# Approach : Here, we are trying to calculate left side and right side of the node, find their height and compare sum of left and right with the maxval. The probelm is done in the same way as calculating the height, the only 
# catch is we are calculating the diameter by adding left and right value and returning the max of those summation value.
# Time Complexity : O(n)
# Space Complexity : O(h)


class Solution :    
    def mainmethod(self, root):
        self.maxdia = 0
        self.diameterofBT(root)
        return self.maxdia

    def diameterofBT(self, root):    
        if root is None:
            return 0

        left = self.diameterofBT(root.left)
        right = self.diameterofBT(root.right)
        self.maxdia = max(self.maxdia, left+right)
        return 1 + max(left, right)
