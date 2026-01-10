# LeetCode #35: Search Insert Position
# Approach : since this is a sorted array, we will first find the mid number, if mid number is greater than equal to the target we will put mid as ans and decrement the high to mid -1 else increment the low to mid +1. we will repeat the proces
# until r < l.
# Time Complexity : O(log n)  
class Solution:
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        ans = len(nums)
        while l <= r:
            mid = (l +r)//2
            if nums[mid] >= target:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans            
