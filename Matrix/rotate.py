# Leetcode 48. Rotate Image
# Approach : we are asked to rotate the matrix by 90 degrees.That means rows should be converted into columns and then they are ordered in reversed direction.therefore, we first find out the transpose of the matrix and then
# reversed each row.
# Time complexity: O(n**2) since the given matrix is a square matrix
# Space complexity:O(1)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:   
            row.reverse()


        return  matrix           
