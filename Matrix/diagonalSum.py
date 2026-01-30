# Leetcode 1572. Matrix Diagonal Sum
# Approach : Iterate on the length of the matrix. add the matrix value to the sum only when row index and col index is same. when they are same, find the anti diagonal by len(matrix) -1 -i. chec if it is not equal to i , add the element to the sum
# Time complexity : O(n), where n is the length of matrix
# Space Complexity : 0(1)

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sumn = 0
        n = len(mat)
        for i in range(n):
            sumn += mat[i][i]
            revmat = n -1 -i
            if i != revmat:
                sumn += mat[i][revmat]
        return sumn 
