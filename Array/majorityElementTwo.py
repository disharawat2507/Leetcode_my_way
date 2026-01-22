# Leetcode 229 Majority Element II
# Goal: Find out all the elements which occurs more than n//3 times in the list
# Approach: in hashmap keep on storing the number of times an element is in the list. when the count increase ny n//3, add it in the result array. Return the result.
# Time Complexity : O(n)
# Space Complexity: O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap ={}
        res =[]
        n = len(nums) // 3
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i],0)+1
            if hashmap[nums[i]] > n and nums[i] not in res:
                res.append(nums[i])

        return res        
        
