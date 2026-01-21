# Leetcode 53. Maximum Subarray
# Approach: everytime we will check if the num is greater or the sum of currentsum and num is greater to find the currentsum. Then the max sum will be the max of maxsum and currentsum.
# Time Complexity : O(n)
# Space Complexity : O(1)

class Solution:
  
    def maxSubArray(self, nums: List[int]) -> int:
        currentsum = nums[0]
        maxsum = nums[0]
        for i in range(1, len(nums)):
            currentsum = max(nums[i], currentsum + nums[i])
            maxsum = max(currentsum, maxsum)
        return maxsum   
