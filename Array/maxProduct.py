# Leetcode 152. Maximum Product Subarray
# Approach: we will calculate the products from start and back, which every is max will will store in res. in case, we get 0 in between , reset prefix to 1 and 0 for suffix, reset suffix to 1.
#   Finally return the answer
# Time Complexity: O(n)
# Space Complexity : O(1) 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -sys.maxsize
        prefix , suffix =1,1
        for i in range(len(nums)):
            if prefix == 0:
                prefix =1
            elif suffix == 0:
                suffix =1
            prefix = prefix *nums[i]
            suffix = suffix * nums[len(nums)-i -1]
            res = max(res, max(prefix, suffix))

        return res            
        
