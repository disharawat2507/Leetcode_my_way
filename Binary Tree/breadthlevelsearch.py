# Breadth first traversal.
# Approach : In BFS, we use queue. I have imported deque from collection library.And will add root in it at the  begining. Everytime check if queue has some value or not. if it has the value, pull out the value using popleft()
# check if the node has any left or right nodes attached to it, if yes, add them in the queue.Add the node value to the result where we arrange the values of node in BFS fashion.
# Time Complexity : O(n)
# Space Complexity : O(w) where w is the width of the tree. worst case O(n)


from collections import deque
class Solution:
    def breadthlevelsearch(self, root):
        if root is None:
            return 
        result =[]   
        queue = deque([root])
        while queue: 
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right) 

        return result  
