# Approach : We have to find the ceil that means the node value greater than equal to the target. we will iterate on the curr node and keep on updating its value based on smaller or bigger than the target value.
#   once we get the node equal to target val we return the node value, else we return the just greater value than the node val.
# Time Complexity : O(h) , height of the tree
# Space Complexity : O(1), since we are iterating on the tree


class Solution:
    def findCeil(self,root, target) :
        ceil = -1
        curr = root
        while curr:
            if curr.val < target:
                curr = curr.right
                
            elif curr.val > target:
                
                ceil = curr.val
                curr = curr.left
                
            elif curr.val == target:
                ceil = target
                return ceil

        return ceil  
