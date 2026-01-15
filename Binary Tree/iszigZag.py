# Leetcode 103: Binary Tree Zigzag Level Order Traversal.
# Approach : We use a boolean flag (or pointer) to determine the direction for storing node values. In each iteration, we check the value of lefttoright to calculate the appropriate index within the row. 
# To ensure efficiency, the row is initialized with a fixed length equal to the current size of the queue.
# Time complexity : O(n)
# Space Complexity : O(n)

from collections import deque
class Solution :
    def iszigZag(self,root):
        queue = deque([root])
        lefttoright = True
        result = []
        if root is None:
            return result
        while queue:
            size = len(queue)
            row =[0] * size
            for i in range(size):
                node = queue.popleft()
                idx = i if lefttoright else (size -1 -i)
                row[idx] = node.val
                if node.left :
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            lefttoright = not lefttoright
            result.append(row)
        return result  
