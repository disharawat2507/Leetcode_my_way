# Leetcode 1. Two Sum
# Approach : we have utilized hashmap which will store the num value and its index, if target val is equal to some stored value in the map, we will return the current idex and the value of index from the map.
# Time Complexity : O(n)
# Space Complexity : O(n)

class Solution:
    def twoSum(self,nums1, target):
        hashmap = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in hashmap :  
                return [i,hashmap[val]]
            else:
                hashmap[nums[i]] = i 

        return [-1,-1] 
