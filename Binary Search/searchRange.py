# Leetcode 34:  Find First and Last Position of Element in Sorted Array
# Approach : We use lower bound and upper bound approach. In lower bound approach, we find the index of the first occurence of target, if firstidx != target, or floor != - 1 , return [-1,-1] . Do upper bound approach for 
#        highest index, ceil . in upper bound, find the first max num, if it is there , put it in ceil, return ceil - 1.
# Time Complexity : O(log n)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) -1
        floor = -1
        ceil = len(nums)
        
        while r >= l:
            mid = (r+l) // 2
            if nums[mid] >= target:
                floor = mid
                r = mid - 1
            else:
                l = mid +1

        if floor == -1 or nums[floor] !=target:
            return [-1,-1]

        l = 0
        r = len(nums) - 1
        while r >= l:
            mid = (r+l)//2
            if nums[mid] > target:
                ceil = mid
                r = mid - 1
            else:
                l = mid +1

        return [floor, ceil -1]            


        
