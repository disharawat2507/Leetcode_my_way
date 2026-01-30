# Leetcode 867. Transpose Matrix
# Approach : we have to make a res matrix where the number of rows = number of columns of given matrix and number of cols of given matrix = number of rows. then iterate on rows and columns, for each res[i][j] = matrix[j][i]
# Time Compelxity : O(n*m) n, m are number of rows and columns
# space Complexity : O(n*m) n, m are the number of rows and columns

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        res =[[0]*n for i in range(m)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res[j][i] = matrix[i][j]

        return res 
