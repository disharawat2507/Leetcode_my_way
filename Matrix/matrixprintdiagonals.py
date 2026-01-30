# Approach : We are asked to print the diagonals in the given matrix. We will iterate through rows and columns and check the condition where the row index == column index. when both are equal print the element.
# Time Complexity : O(n * m) where n and m are the number of rows and number of columns
# Space Complexity : O(1)
# example : given matrix : [[5,10,8],[7,6,3],[2,1,9]]
# result : 
# 5 * * 
# * 6 * 
# * * 9 

class Solution:
    def matrixprintdiagonals(self, nums):
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if i == j:
                    print(nums[i][j], end =' ')
                else :
                    print(('*'), end =' ') 
            print()
