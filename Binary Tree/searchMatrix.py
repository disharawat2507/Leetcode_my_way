# Leetcode 74. Search a 2D Matrix
# Approach : In this approach we will utilize the given fact that matrix is sorted. so on row level itself, we will check if the target is greater than 1st index of the row and smaller than last index of the row. if yes, then we will iterate
# on all the columns of that row, else will keep on checking other rows.
# Time Complexity : O(n+m)
# Space Complexity : O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        for i in range(0,n):
            if matrix[i][0] < target and matrix[i][m-1] < target:
                continue    
            elif matrix[i][0] <= target <= matrix[i][m-1]:
                for j in range(m):
                    if matrix[i][j] == target:
                        return True

        return False   
