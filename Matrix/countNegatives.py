# 1351. Count Negative Numbers in a Sorted Matrix
# Approach : I have utilized the fact that rows and cols are both sorted, so if the 1st element is negative, i will count the whole row and move up, same goes for cols as well.
# Time Complexity: O(m+n), m ,n are the number of rows, cols
# Space Complexity : O(1)

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)
        m = len(grid[0])
        r = n-1 
        c = 0

        while r>= 0 and c < m:
            if grid[r][c] < 0:
                count += m -c
                r -=1
            else:
                c +=1
        return count  
