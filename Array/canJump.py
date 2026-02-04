# Leetcode 55. Jump Game
# Approach : we have to find out if we can reach the end of the list. so what i did was i keep on finding the max jumps i can take from an idex by affing the index value and the number on it. if at any point, the max value is
# greater than the length of the numbers,that means i reached/crossed the end. 
# Time Complexity : O(n)
# Space Complexity : O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxidx = 0
        for i in range(len(nums)):
            if maxidx < i :
                return False
            else:
                maxidx = max(maxidx, i+nums[i])
                if maxidx >=len(nums) :
                    return True
        return True  
