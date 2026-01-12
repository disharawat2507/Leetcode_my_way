# Leetcode: 977 Squares of a Sorted Array
# Approach : We will fllow 2 pointer approach so that this can be done in O(n) time complexity. Take 2 pointers, l = 0, r = len(nums)-1. now loop over the array from backwards, if absolute value of nums[l] is less than absolute value at len(nums)-1, we will consider 
# element at len(nums)-1. square it and place it at n-1th position in the result array. and reduce one value from r. otherwise, we wll consider the left element, do the same and increment left index by 1. once the loop completes we will return the result. Result is 
# a sorted array with squares of the array provided in the question.
# Time Complexity : O(n)
# Space Complexity : O(n)


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        res = [0] * len(nums)
        n = len(nums)
        r = len(nums) -1
        for i in range(n-1,-1,-1):
            if abs(nums[l]) < abs(nums[r]):
                num = nums[r]
                r -=1
            else:
                num = nums[l]
                l +=1
            res[i] = num * num

        return res 
