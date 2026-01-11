# This is not a leetcode problem.
# Question :Given a sorted array nums and an integer x. Find the floor and ceil of x in nums. The floor of x is the largest element in the array which is smaller than or equal to x. 
#           The ceiling of x is the smallest element in the array greater than or equal to x. If no floor or ceil exists, output -1.  
# Approach :  use 2 pointers, one at start and another at end of the array. find mid of the array, and start checking if mid of the array is less than equal to the target. if yes, put the value in floor, move left to mid +1
# accordingly if mid num is greater than equal to target, ceil is that num and move right pointer to mid index -1.
# Time Complexity : O(log n) 

class Solution:
    def getFloorAndCeil(self, nums, x):
        l = 0
        r = len(nums) -1
        floor = -1
        ceil = -1
        while r >= l:
            mid = (l+r)//2
            if nums[mid] <= x:
                floor = nums[mid]
                l = mid +1
            elif nums[mid] >=x:
                ceil = nums[mid]
                r = mid -1

        return [floor, ceil]     
