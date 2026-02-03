# Leetcode 153. Find Minimum in Rotated Sorted Array
# Approach : we always find the mid and check if the left part is sorted or not. sorted will be identified if the first element in the left is smaller than the mid element.same check we can have for the right.if the left is sorted 
# compare put the min value as the left and move left to mid+1 else, put the min as mid element and move right to mid-1. 
# Time complexity : O(log n)
# Space Compolexity : O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums)-1
        result = sys.maxsize
        while l <= h:
            mid = (l+h)//2
            if (nums[l] <= nums[mid]):
                result = min(result,nums[l])
                l = mid+1
            else:
                result = min(result, nums[mid])
                h = mid-1

        return result            
