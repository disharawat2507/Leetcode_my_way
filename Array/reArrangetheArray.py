# Leetcode 2149: Rearrange Array Elements by Sign.
# Approach: We know that positive numbers has to be on positive idx n negative numbers on neg idx. so we have created 2 indexes, result array. where we are checking if element is negative, placing in neg
# index and incrementing counter by 2, same goes for positive element. returning the result array.
# Time Complexity : O(n)
# Space Complexity : O(n)

class Solution:
    def reArrangetheArray(self, nums):
        n = len(nums)
        res = [0]* n 
        positiveIdx = 0
        negIdx = 1
        for i in range(n):
            if nums[i] < 0:
                res[negIdx] = nums[i]
                negIdx +=2
            else:
                res[positiveIdx] = nums[i]
                positiveIdx += 2

        return res  
