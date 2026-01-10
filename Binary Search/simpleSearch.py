# LeetCode #704
# Approach : This is a simple binary search where we find the middle number in a sorted array. Then compare if the target is bigger or smaller than the mid.Accordingly we adjust the low and high and return. If the target doesnot exists, 
# we return -1.
# Time Complexity : O(log n)

class Solution:
    def search(self, nums, target):
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r) //2
            if (nums[mid] == target):
                return mid
            elif nums[mid] > target:
                l = mid +1
            else:
                r = mid -1

        return -1    
