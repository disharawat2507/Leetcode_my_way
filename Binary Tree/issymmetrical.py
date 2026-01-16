Leetcode 101: Symmetric Tree.
Approach : keep on checking if both the roots reached the end of leaf nodes or are everytime same. We continously calls the method where we give left of one tree and right of other And right of one tree and left of 
other.
Time Complexity : O(n), n is the number of nodes
Space Complexity: O(h), h is the height of the tree
class Solution:
    def issymmetrical(self, ltree, rtree):
        if not ltree and not rtree:
            return True
        if not ltree or not rtree or ltree.val != rtree.val:
            return False

        return self.issymmetrical(ltree.left,rtree.right) and self.issymmetrical(ltree.right, rtree.left)        
