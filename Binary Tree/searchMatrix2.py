# Leetcode 240. Search a 2D Matrix II
# Approach : we know here that all the rows and columns are sorted. so we will start from first row n last column, if that element is less than the target, then we will move to the next row, else we will reduce the column.
# Time complexity : O(n +m)
# Space Complexity : O(1)

class Solution:
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        r = 0
        c = m -1
        while r < n and c >= 0 :
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r +=1
            else:
                c -=1
        return False           
