# Approach : we are asked to print elements of matrix which are in the lower side of the diagonal. Iterate through rows and columns, put a condition to print elements only till j <= i , else print stars.
# Time Complexity : O(n*m) n and m are the number of rows and columns
# Space Complexity : O(1)

class Solution:
    def matrixlowertriangle(self, nums):
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if j > i:
                    print('*', end =' ')
                else:    
                    print(nums[i][j], end =' ')
            print()    

s = Solution()
nums = [[5,10,8],[7,6,3],[2,1,9]]
s.matrixuppertriangle(nums)
