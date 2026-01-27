# Leetcode 938. Range Sum of BST
# Approach : We are using BFS, so i will insert node everytime and check its values are greater than both low and high, then i will append its left to the queue, else if it is greater than both low and high, i will append
# its right in the queue. Else i will add the node val to the sum and append both its left and right in the queue. Return the sum in the end
# Time Complexity: O(n) n is the number of nodes in worst scenerio.
# Space Complexity: O(w) w is the width of the binary search tree.

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        sumn = 0
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                if node.val > low and node.val > high:
                    queue.append(node.left)
                elif node.val < low and node.val < high:
                    queue.append(node.right)
                else:
                    sumn += node.val
                    queue.append(node.left)
                    queue.append(node.right)

        return sumn
