# Approach : We have asked to print only upper part of the matrix from diagonal. the lower part should be replaced by *. So what I have done is i looped over the rows and then columns and put a condition that if each row index is less than column index then
# print the element else print *
# Time Complexity: O(n*m) where n is number of rows and m is the number of columns
# Space Complexity : O(1)
class Solution:
    def matrixuppertriangle(self, nums):
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if j < i:
                    print('*', end =' ')
                else:    
                    print(nums[i][j], end =' ')
            print()    

s = Solution()
nums = [[5,10,8],[7,6,3],[2,1,9]]
s.matrixuppertriangle(nums)
