# We have to find out how many times the array is rotated
# Approach : we will everytime find the middle and check if lowest value is smaller than the one in the result. if yes, we will put the lowest index as answer else, the mid index(lowest from right side) into the answer.
# Time complexity : O(log n)
# Space Compelxity : O(1)

class Solution:
    def findKRotation(self, nums):
        l = 0
        h = len(nums)-1
        count = 0
        ans = sys.maxsize
        while l <= h:
            mid = (l+h) // 2
            if nums[l] <= nums[mid]:
                if nums[l] < ans:
                    count = l
                    ans = min(ans,nums[l])
                l = mid+1
            else:
                if nums[mid] < ans:
                    count = mid
                    ans = min(ans, nums[mid])
                h = mid - 1
        return count            

