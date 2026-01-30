# Leetcode 766. Toeplitz Matrix
# Approach : we are iterating from row 1 and col 1 to the length of row and columns and always checking if the row just above and 1 column behind are same or not. If not same return False
# Time Complexity: O(n*m)
# Space Complexity: O(1)

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        for r in range(1,n):
            for j in range(1,m):
                if matrix[r][j] != matrix[r-1][j-1]:
                    return False

        return True   
