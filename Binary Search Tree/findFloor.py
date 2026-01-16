# Approach : We are trying to find the floor ie; value less than or equal to target. We will keep on assign the value to floor whenever target is greater than the current node val, if not, we will move towards left.
# At the end we will return the floor value else -1.
# Time complexity : O(h) , h is the height of the tree
# Space Complexity : O(1), we are using iterative approach so no space used.  


class Solution:
    def findFloor(self,root, target) :
        floor = -1
        curr = root
        while curr:
            if curr.val < target:
                floor = curr.val
                curr = curr.right
            elif curr.val > target:               
                curr = curr.left
            elif curr.val == target:
                floor = curr.val
                return floor

        return floor 
